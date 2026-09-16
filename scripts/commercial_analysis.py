#!/usr/bin/env python3
"""Commercial analysis recipes with explicit input contracts.

Standard library only (Python 3.8+). Every recipe validates its inputs, fails with a
useful error code instead of producing plausible-looking output, reconciles its
components to the observed total, and records calculation provenance.

Recipes
  profile       Data profiling: columns, missingness, duplicates at a declared grain,
                negative/zero values, units per key.
  pvm           Revenue bridge: price, volume, mix, new and discontinued items.
  buyers        Volume = [eligible population x penetration] x buyers' purchase
                occasions per buyer x units per occasion, with an order-independent
                (Shapley) attribution.
  contribution  Contribution to change and share by group (segment, channel, region,
                SKU or brand), with consistent denominators.
  join-check    Key coverage and fan-out check before joining two tables.

Arithmetic decompositions locate where a change arose under a declared convention.
They do not identify causes. See references/analytics.md.

Exit codes: 0 ok, 2 data-contract error (JSON error on stdout), 1 unexpected failure.
"""

import argparse
import csv
import datetime
import hashlib
import itertools
import json
import math
import sys
from decimal import Decimal, InvalidOperation
from fractions import Fraction

SCRIPT_VERSION = "1.0.0"
MISSING_TOKENS = {"", "na", "n/a", "null", "none", "nan", "-"}


class DataContractError(Exception):
    def __init__(self, code, message, details=None):
        super().__init__(message)
        self.code = code
        self.message = message
        self.details = details or {}


# ---------------------------------------------------------------------------
# Input helpers
# ---------------------------------------------------------------------------

def read_csv(path):
    try:
        with open(path, newline="", encoding="utf-8-sig") as handle:
            reader = csv.DictReader(handle)
            if reader.fieldnames is None:
                raise DataContractError("EMPTY_FILE", "Input file has no header row.", {"file": path})
            fieldnames = [name.strip() for name in reader.fieldnames]
            if len(set(fieldnames)) != len(fieldnames):
                raise DataContractError("DUPLICATE_COLUMNS", "Header contains duplicate column names.", {"columns": fieldnames})
            rows = []
            for line_number, raw in enumerate(reader, start=2):
                row = {}
                for key, value in raw.items():
                    if key is None:
                        raise DataContractError("RAGGED_ROW", "Row has more values than header columns.", {"line": line_number})
                    row[key.strip()] = value.strip() if isinstance(value, str) else value
                row["__line__"] = line_number
                rows.append(row)
    except FileNotFoundError:
        raise DataContractError("FILE_NOT_FOUND", "Input file not found.", {"file": path})
    return fieldnames, rows


def file_sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def is_missing(value):
    return value is None or str(value).strip().lower() in MISSING_TOKENS


def parse_number(value, column, line):
    text = str(value).strip()
    if "," in text:
        raise DataContractError(
            "AMBIGUOUS_NUMBER_FORMAT",
            "Number contains a comma; thousands and decimal separators are ambiguous. Clean the column to plain digits with '.' as decimal point.",
            {"column": column, "line": line, "value": text},
        )
    try:
        number = Decimal(text)
    except InvalidOperation:
        raise DataContractError("NON_NUMERIC_VALUE", "Value is not numeric.", {"column": column, "line": line, "value": text})
    if not number.is_finite():
        raise DataContractError("NON_NUMERIC_VALUE", "Value is not a finite number.", {"column": column, "line": line, "value": text})
    return Fraction(number)


def require_columns(fieldnames, columns):
    missing = [c for c in columns if c and c not in fieldnames]
    if missing:
        raise DataContractError("MISSING_COLUMNS", "Required columns are not in the header.", {"missing": missing, "available": fieldnames})


def split_cols(text):
    return [c.strip() for c in text.split(",") if c.strip()] if text else []


def to_float(value, places=10):
    if value is None:
        return None
    return round(float(value), places)


def pct(numerator, denominator):
    if denominator == 0:
        return None
    return to_float(Fraction(numerator) / Fraction(denominator) * 100, 6)


def check_periods(rows, period_col, base, current):
    present = {r[period_col] for r in rows}
    missing = [p for p in (base, current) if p not in present]
    if missing:
        raise DataContractError("PERIOD_NOT_FOUND", "Requested period(s) not present in the data.", {"missing": missing, "present": sorted(present)})
    if base == current:
        raise DataContractError("SAME_PERIOD", "Base and current periods must differ.", {"period": base})


def check_period_lengths(rows, period_col, days_col, base, current, allow_unequal):
    if not days_col:
        return None
    lengths = {}
    for r in rows:
        if r[period_col] in (base, current):
            if is_missing(r.get(days_col)):
                raise DataContractError("MISSING_VALUES", "Period length is missing.", {"column": days_col, "line": r["__line__"]})
            lengths.setdefault(r[period_col], set()).add(parse_number(r[days_col], days_col, r["__line__"]))
    for period, values in lengths.items():
        if len(values) > 1:
            raise DataContractError("INCONSISTENT_PERIOD_LENGTH", "Rows within one period declare different lengths.", {"period": period, "lengths": sorted(to_float(v) for v in values)})
    base_len, cur_len = next(iter(lengths[base])), next(iter(lengths[current]))
    if base_len != cur_len and not allow_unequal:
        raise DataContractError(
            "PERIOD_LENGTH_MISMATCH",
            "Base and current periods have different lengths; totals are not comparable. Normalise to a common length or pass --allow-unequal-periods and interpret per-day values.",
            {"base_days": to_float(base_len), "current_days": to_float(cur_len)},
        )
    return {"base_days": to_float(base_len), "current_days": to_float(cur_len), "equal": base_len == cur_len}


def single_value(rows, column, code, label):
    if not column:
        return None
    values = {r[column] for r in rows}
    if len(values) > 1:
        raise DataContractError(code, "Multiple {} values in the rows being compared.".format(label), {"column": column, "values": sorted(values)})
    return next(iter(values)) if values else None


def provenance(args, path, rows_read, rows_used, extra=None):
    info = {
        "file": path,
        "sha256": file_sha256(path),
        "rows_read": rows_read,
        "rows_used": rows_used,
        "arguments": {k: v for k, v in vars(args).items() if k not in ("func",)},
        "script": "scripts/commercial_analysis.py",
        "script_version": SCRIPT_VERSION,
        "generated_at": datetime.datetime.now(datetime.timezone.utc).replace(microsecond=0).isoformat(),
    }
    if extra:
        info.update(extra)
    return info


def reconcile(observed, components, tolerance):
    total = sum(components.values(), Fraction(0))
    residual = total - observed
    ok = abs(residual) <= Fraction(Decimal(str(tolerance)))
    result = {
        "observed_change": to_float(observed),
        "sum_of_components": to_float(total),
        "residual": to_float(residual),
        "tolerance": tolerance,
        "reconciles": ok,
    }
    if not ok:
        raise DataContractError("RECONCILIATION_FAILED", "Components do not reconcile to the observed change within tolerance.", result)
    return result


# ---------------------------------------------------------------------------
# profile
# ---------------------------------------------------------------------------

def run_profile(args):
    fieldnames, rows = read_csv(args.input)
    grain = split_cols(args.grain)
    require_columns(fieldnames, grain + [c for c in (args.unit_col, args.key_col, args.period_col) if c])
    columns = {}
    for col in fieldnames:
        values = [r.get(col) for r in rows]
        missing = sum(1 for v in values if is_missing(v))
        numeric, negatives, zeros, minimum, maximum = 0, 0, 0, None, None
        for v in values:
            if is_missing(v):
                continue
            try:
                n = Fraction(Decimal(str(v)))
            except (InvalidOperation, ValueError):
                continue
            numeric += 1
            negatives += n < 0
            zeros += n == 0
            minimum = n if minimum is None or n < minimum else minimum
            maximum = n if maximum is None or n > maximum else maximum
        present = len(values) - missing
        columns[col] = {
            "non_missing": present,
            "missing": missing,
            "distinct": len({v for v in values if not is_missing(v)}),
            "numeric_share_of_present": pct(numeric, present) if present else None,
            "negatives": negatives if numeric else None,
            "zeros": zeros if numeric else None,
            "min": to_float(minimum),
            "max": to_float(maximum),
        }
    duplicates = []
    if grain:
        seen = {}
        for r in rows:
            key = tuple(r[c] for c in grain)
            seen.setdefault(key, []).append(r["__line__"])
        duplicates = [{"key": list(k), "lines": v} for k, v in seen.items() if len(v) > 1]
    unit_changes = []
    if args.unit_col and args.key_col:
        units = {}
        for r in rows:
            units.setdefault(r[args.key_col], set()).add(r[args.unit_col])
        unit_changes = [{"key": k, "units": sorted(v)} for k, v in units.items() if len(v) > 1]
    warnings = []
    if duplicates:
        warnings.append("Duplicate rows at the declared grain: aggregate deliberately or add the missing grain column before analysis.")
    if unit_changes:
        warnings.append("Some keys use more than one unit; convert to a common unit before volume or price analysis.")
    for col, info in columns.items():
        if info["missing"]:
            warnings.append("Column '{}' has {} missing value(s); decide explicitly how to treat them.".format(col, info["missing"]))
    periods = sorted({r[args.period_col] for r in rows}) if args.period_col else None
    return {
        "recipe": "profile",
        "status": "ok",
        "results": {
            "rows": len(rows),
            "columns": columns,
            "grain": grain,
            "duplicate_keys_at_grain": duplicates[:50],
            "duplicate_key_count": len(duplicates),
            "periods": periods,
            "keys_with_unit_changes": unit_changes[:50],
        },
        "warnings": warnings,
        "interpretation_limits": ["Profiling describes the file; it does not validate definitions, coverage or source truth."],
        "provenance": provenance(args, args.input, len(rows), len(rows)),
    }


# ---------------------------------------------------------------------------
# pvm
# ---------------------------------------------------------------------------

def run_pvm(args):
    fieldnames, rows = read_csv(args.input)
    dims = split_cols(args.dims)
    if not args.revenue_col and not args.price_col:
        raise DataContractError("MISSING_ARGUMENT", "Provide --revenue-col, --price-col, or both.")
    needed = [args.key, args.period_col, args.quantity_col, args.revenue_col, args.price_col, args.unit_col, args.currency_col, args.period_days_col] + dims
    require_columns(fieldnames, needed)
    check_periods(rows, args.period_col, args.base, args.current)
    scoped = [r for r in rows if r[args.period_col] in (args.base, args.current)]
    outside = len(rows) - len(scoped)
    period_lengths = check_period_lengths(scoped, args.period_col, args.period_days_col, args.base, args.current, args.allow_unequal_periods)

    value_cols = [c for c in (args.quantity_col, args.revenue_col, args.price_col) if c]
    missing_rows = [r["__line__"] for r in scoped if any(is_missing(r.get(c)) for c in value_cols)]
    excluded = []
    if missing_rows:
        if not args.exclude_missing:
            raise DataContractError(
                "MISSING_VALUES",
                "Rows in the compared periods have missing quantity, price or revenue. Fix them or pass --exclude-missing to exclude them explicitly (results will be marked partial).",
                {"lines": missing_rows[:100], "count": len(missing_rows)},
            )
        excluded = missing_rows
        scoped = [r for r in scoped if r["__line__"] not in set(missing_rows)]

    currency = single_value(scoped, args.currency_col, "MIXED_CURRENCY", "currency")
    grain = dims + [args.key, args.period_col]
    seen = {}
    for r in scoped:
        seen.setdefault(tuple(r[c] for c in grain), []).append(r["__line__"])
    dups = [{"key": list(k), "lines": v} for k, v in seen.items() if len(v) > 1]
    if dups:
        raise DataContractError("DUPLICATE_GRAIN", "More than one row per item and period at the declared grain. Aggregate deliberately or add the missing grain column via --dims.", {"grain": grain, "duplicates": dups[:50]})

    items = {}
    units_by_item = {}
    tol = Fraction(Decimal(str(args.tolerance)))
    for r in scoped:
        line = r["__line__"]
        item = tuple(r[c] for c in dims + [args.key])
        q = parse_number(r[args.quantity_col], args.quantity_col, line)
        if q < 0:
            raise DataContractError("NEGATIVE_VALUES", "Negative quantity. Treat returns explicitly before decomposition.", {"line": line, "column": args.quantity_col})
        rev = parse_number(r[args.revenue_col], args.revenue_col, line) if args.revenue_col else None
        price = parse_number(r[args.price_col], args.price_col, line) if args.price_col else None
        if (rev is not None and rev < 0) or (price is not None and price < 0):
            raise DataContractError("NEGATIVE_VALUES", "Negative price or revenue.", {"line": line})
        if rev is None:
            rev = price * q
        if price is None:
            if q == 0:
                if rev != 0:
                    raise DataContractError("ZERO_QUANTITY_WITH_REVENUE", "Revenue recorded with zero quantity; price is undefined. Check returns, credit notes or unit definitions.", {"line": line, "item": list(item)})
                price = None
            else:
                price = rev / q
        elif abs(price * q - rev) > tol:
            raise DataContractError("PRICE_REVENUE_MISMATCH", "price x quantity does not equal revenue within tolerance. Check gross/net definitions, discounts or units.", {"line": line, "price_x_quantity": to_float(price * q), "revenue": to_float(rev)})
        if args.unit_col:
            units_by_item.setdefault(item, set()).add(r[args.unit_col])
        period = "base" if r[args.period_col] == args.base else "current"
        items.setdefault(item, {})[period] = {"q": q, "r": rev, "p": price}

    unit = None
    if args.unit_col:
        changed = [{"item": list(k), "units": sorted(v)} for k, v in units_by_item.items() if len(v) > 1]
        if changed:
            raise DataContractError("UNIT_CHANGE", "An item's unit differs between rows or periods. Convert to a common unit first.", {"items": changed[:50]})
        all_units = {next(iter(v)) for v in units_by_item.values()}
        if len(all_units) > 1:
            raise DataContractError("MIXED_UNITS", "Items use different units, so volume and mix cannot be aggregated. Convert to a common volume unit (e.g. litres or standard cases) first.", {"units": sorted(all_units)})
        unit = next(iter(all_units)) if all_units else None

    zero = Fraction(0)
    base_total = sum((v["base"]["r"] for v in items.values() if "base" in v), zero)
    cur_total = sum((v["current"]["r"] for v in items.values() if "current" in v), zero)
    change = cur_total - base_total

    continuing, new, discontinued, inactive = [], [], [], []
    for item, v in items.items():
        q0 = v.get("base", {}).get("q", zero)
        q1 = v.get("current", {}).get("q", zero)
        if q0 > 0 and q1 > 0:
            continuing.append(item)
        elif q0 == 0 and q1 > 0:
            new.append(item)
        elif q0 > 0 and q1 == 0:
            discontinued.append(item)
        else:
            inactive.append(item)

    q0c = sum((items[i]["base"]["q"] for i in continuing), zero)
    q1c = sum((items[i]["current"]["q"] for i in continuing), zero)
    r0c = sum((items[i]["base"]["r"] for i in continuing), zero)
    r1c = sum((items[i]["current"]["r"] for i in continuing), zero)
    avg_p0 = r0c / q0c if q0c else zero
    price_at_current_q = sum(((items[i]["current"]["p"] - items[i]["base"]["p"]) * items[i]["current"]["q"] for i in continuing), zero)
    price_at_base_q = sum(((items[i]["current"]["p"] - items[i]["base"]["p"]) * items[i]["base"]["q"] for i in continuing), zero)
    interaction = price_at_current_q - price_at_base_q
    volume = (q1c - q0c) * avg_p0
    mix = sum((items[i]["current"]["q"] * items[i]["base"]["p"] for i in continuing), zero) - q1c * avg_p0
    new_effect = sum((items[i]["current"]["r"] for i in new), zero)
    disc_effect = -sum((items[i]["base"]["r"] for i in discontinued), zero)

    if args.interaction == "separate":
        components = {"price": price_at_base_q, "price_volume_interaction": interaction, "volume": volume, "mix": mix, "new_items": new_effect, "discontinued_items": disc_effect}
    else:
        components = {"price": price_at_current_q, "volume": volume, "mix": mix, "new_items": new_effect, "discontinued_items": disc_effect}
    rec = reconcile(change, components, args.tolerance)
    continuing_rec = (r1c - r0c) - (price_at_current_q + volume + mix)
    if abs(continuing_rec) > tol:
        raise DataContractError("RECONCILIATION_FAILED", "Continuing-item components do not reconcile.", {"residual": to_float(continuing_rec)})

    item_rows = []
    for item, v in sorted(items.items()):
        b, c = v.get("base"), v.get("current")
        status = "continuing" if item in continuing else "new" if item in new else "discontinued" if item in discontinued else "inactive_both_periods"
        row = {
            "item": list(item),
            "status": status,
            "base_quantity": to_float(b["q"]) if b else None,
            "current_quantity": to_float(c["q"]) if c else None,
            "base_price": to_float(b["p"]) if b and b["p"] is not None else None,
            "current_price": to_float(c["p"]) if c and c["p"] is not None else None,
            "base_revenue": to_float(b["r"]) if b else None,
            "current_revenue": to_float(c["r"]) if c else None,
            "revenue_change": to_float((c["r"] if c else zero) - (b["r"] if b else zero)),
            "revenue_growth_pct": pct((c["r"] if c else zero) - b["r"], b["r"]) if b and b["r"] else None,
        }
        if status == "continuing":
            row["price_effect_at_current_quantity"] = to_float((c["p"] - b["p"]) * c["q"])
            row["quantity_effect_at_base_price"] = to_float((c["q"] - b["q"]) * b["p"])
        if row["revenue_growth_pct"] is None and status != "continuing":
            row["growth_note"] = "not computed: no base revenue" if status == "new" else "not computed"
        item_rows.append(row)

    flags = []
    total_q0 = sum((v["base"]["q"] for v in items.values() if "base" in v), zero)
    total_q1 = sum((v["current"]["q"] for v in items.values() if "current" in v), zero)
    if change > 0 and total_q1 < total_q0:
        flags.append("Revenue grew while total volume fell: growth is price- and/or mix-led. Check margin, elasticity and whether volume loss is a leading indicator.")
    if components["price"] > 0 and volume < 0:
        flags.append("Positive price effect with negative volume effect on continuing items.")
    if abs(mix) > abs(volume) and mix != 0:
        flags.append("Mix effect exceeds volume effect: portfolio or channel composition changed materially.")
    if new or discontinued:
        flags.append("New or discontinued items present: their revenue is reported separately, not as growth rates.")
    if excluded:
        flags.append("Rows were excluded for missing values: results cover a partial dataset.")

    warnings = []
    if not args.unit_col:
        warnings.append("No --unit-col declared: volume is assumed to be in one common unit across items. Verify before interpreting volume and mix.")
    if args.revenue_basis == "unknown":
        warnings.append("Revenue basis (gross/net) not declared.")
    if outside:
        warnings.append("{} row(s) belong to other periods and were not part of this comparison.".format(outside))

    return {
        "recipe": "pvm",
        "status": "ok",
        "coverage": "partial" if excluded else "complete",
        "convention": {
            "items": "an item is the combination of --dims and --key",
            "continuing_items": "quantity > 0 in both periods",
            "price_effect": "sum over continuing items of (current price - base price) x current quantity" if args.interaction != "separate" else "sum over continuing items of (current price - base price) x base quantity",
            "interaction": "allocated to the price effect" if args.interaction != "separate" else "reported separately as (price change) x (quantity change)",
            "volume_effect": "(current total continuing quantity - base total continuing quantity) x base average price of continuing items",
            "mix_effect": "sum of current quantity x base price, minus current total continuing quantity x base average price",
            "new_items": "current revenue of items with zero or absent base quantity",
            "discontinued_items": "minus base revenue of items with zero or absent current quantity",
            "revenue_basis": args.revenue_basis,
            "currency": currency,
            "volume_unit": unit,
        },
        "results": {
            "base_period": args.base,
            "current_period": args.current,
            "base_revenue": to_float(base_total),
            "current_revenue": to_float(cur_total),
            "revenue_change": to_float(change),
            "revenue_growth_pct": pct(change, base_total),
            "revenue_growth_note": None if base_total else "not computed: base revenue is zero",
            "base_volume": to_float(total_q0),
            "current_volume": to_float(total_q1),
            "volume_growth_pct": pct(total_q1 - total_q0, total_q0),
            "components": {k: to_float(v) for k, v in components.items()},
            "continuing": {
                "items": len(continuing),
                "base_revenue": to_float(r0c),
                "current_revenue": to_float(r1c),
                "base_average_price": to_float(avg_p0),
                "price_effect_at_current_quantity": to_float(price_at_current_q),
                "price_effect_at_base_quantity": to_float(price_at_base_q),
                "price_volume_interaction": to_float(interaction),
                "volume_effect": to_float(volume),
                "mix_effect": to_float(mix),
            },
            "new_items": [list(i) for i in new],
            "discontinued_items": [list(i) for i in discontinued],
            "inactive_items": [list(i) for i in inactive],
            "period_lengths": period_lengths,
            "items": item_rows,
        },
        "reconciliation": rec,
        "flags": flags,
        "warnings": warnings,
        "interpretation_limits": [
            "Arithmetic decomposition under the stated convention: it locates where revenue change arose, not why.",
            "Mix depends on item granularity; a different --dims choice gives a different price/mix split with the same total.",
            "Price effects use realised average price per item (revenue / quantity), which includes promotions and discounts if revenue is net of them.",
        ],
        "provenance": provenance(args, args.input, len(rows), len(scoped), {"excluded_lines": excluded, "rows_outside_periods": outside}),
    }


# ---------------------------------------------------------------------------
# buyers
# ---------------------------------------------------------------------------

def shapley_multiplicative(base, current):
    """Order-independent attribution of a product's change to its factors.

    base and current are dicts factor -> Fraction. Returns dict factor -> Fraction.
    Exact: the attributions sum to product(current) - product(base).
    """
    names = list(base.keys())
    n = len(names)
    effects = {name: Fraction(0) for name in names}
    for name in names:
        others = [x for x in names if x != name]
        for size in range(len(others) + 1):
            weight = Fraction(math.factorial(size) * math.factorial(n - size - 1), math.factorial(n))
            for subset in itertools.combinations(others, size):
                product = Fraction(1)
                for other in others:
                    product *= current[other] if other in subset else base[other]
                effects[name] += weight * (current[name] - base[name]) * product
    return effects


def run_buyers(args):
    fieldnames, rows = read_csv(args.input)
    rates_form = bool(args.frequency_col or args.units_per_occasion_col)
    if rates_form:
        if not (args.frequency_col and args.units_per_occasion_col and args.volume_col):
            raise DataContractError("MISSING_ARGUMENT", "Rates form needs --frequency-col, --units-per-occasion-col and --volume-col.")
        needed = [args.buyers_col, args.frequency_col, args.units_per_occasion_col, args.volume_col]
    else:
        if not (args.occasions_col and args.units_col):
            raise DataContractError("MISSING_ARGUMENT", "Counts form needs --occasions-col and --units-col.")
        needed = [args.buyers_col, args.occasions_col, args.units_col]
    if not args.window_col:
        raise DataContractError("WINDOW_UNDEFINED", "Buyer, frequency and penetration measures need a defined time window. Provide --window-col (e.g. days or a label such as '52w').")
    require_columns(fieldnames, [args.period_col, args.window_col, args.population_col, args.segment_col] + needed)
    check_periods(rows, args.period_col, args.base, args.current)
    scoped = [r for r in rows if r[args.period_col] in (args.base, args.current)]

    segments = {}
    for r in scoped:
        segment = r[args.segment_col] if args.segment_col else "all"
        key = (segment, r[args.period_col])
        if key in segments:
            raise DataContractError("DUPLICATE_GRAIN", "More than one row for a segment and period.", {"segment": segment, "period": r[args.period_col], "lines": [segments[key]["__line__"], r["__line__"]]})
        segments[key] = r

    tol = Fraction(Decimal(str(args.tolerance)))
    results = {}
    for segment in sorted({k[0] for k in segments}):
        pair = {}
        for label, period in (("base", args.base), ("current", args.current)):
            r = segments.get((segment, period))
            if r is None:
                raise DataContractError("PERIOD_NOT_FOUND", "Segment missing a period.", {"segment": segment, "period": period})
            line = r["__line__"]
            for col in needed + ([args.population_col] if args.population_col else []) + [args.window_col]:
                if is_missing(r.get(col)):
                    raise DataContractError("MISSING_VALUES", "Missing value; unknown is not zero.", {"segment": segment, "period": period, "column": col, "line": line})
            buyers = parse_number(r[args.buyers_col], args.buyers_col, line)
            if rates_form:
                freq = parse_number(r[args.frequency_col], args.frequency_col, line)
                upo = parse_number(r[args.units_per_occasion_col], args.units_per_occasion_col, line)
                volume = parse_number(r[args.volume_col], args.volume_col, line)
                implied = buyers * freq * upo
                if abs(implied - volume) > tol:
                    raise DataContractError("IDENTITY_MISMATCH", "buyers x frequency x units per occasion does not equal volume. Definitions, windows or denominators are inconsistent.", {"segment": segment, "period": period, "implied_volume": to_float(implied), "volume": to_float(volume)})
                occasions, units = buyers * freq, volume
            else:
                occasions = parse_number(r[args.occasions_col], args.occasions_col, line)
                units = parse_number(r[args.units_col], args.units_col, line)
            if min(buyers, occasions, units) < 0:
                raise DataContractError("NEGATIVE_VALUES", "Negative buyers, occasions or units.", {"segment": segment, "period": period})
            if buyers != int(buyers):
                raise DataContractError("NON_INTEGER_BUYERS", "Buyer count must be a whole number of unique buyers (weighted panel projections should be supplied as integers or rounded explicitly).", {"segment": segment, "period": period})
            if buyers == 0:
                if units > 0 or occasions > 0:
                    raise DataContractError("UNITS_WITHOUT_BUYERS", "Units or occasions recorded with zero buyers.", {"segment": segment, "period": period})
                raise DataContractError("ZERO_BASE_NOT_DECOMPOSABLE", "Zero buyers in a period: frequency and units per occasion are undefined, so the multiplicative decomposition does not exist. Report buyers and volume directly.", {"segment": segment, "period": period})
            if occasions < buyers:
                raise DataContractError("OCCASIONS_BELOW_BUYERS", "Purchase occasions are fewer than buyers; every buyer must have at least one occasion. Check that both use the same window and population.", {"segment": segment, "period": period})
            record = {"buyers": buyers, "occasions": occasions, "units": units, "window": r[args.window_col], "line": line}
            if args.population_col:
                population = parse_number(r[args.population_col], args.population_col, line)
                if population <= 0:
                    raise DataContractError("INVALID_POPULATION", "Eligible population must be positive.", {"segment": segment, "period": period})
                if buyers > population:
                    raise DataContractError("BUYERS_EXCEED_POPULATION", "Buyers exceed the eligible population; the population definition or buyer count is wrong.", {"segment": segment, "period": period})
                record["population"] = population
            pair[label] = record
        if pair["base"]["window"] != pair["current"]["window"]:
            raise DataContractError("WINDOW_MISMATCH", "Base and current use different time windows; frequency and penetration are not comparable.", {"segment": segment, "base_window": pair["base"]["window"], "current_window": pair["current"]["window"]})

        def factors(rec):
            f = {}
            if "population" in rec:
                f["eligible_population"] = rec["population"]
                f["penetration"] = rec["buyers"] / rec["population"]
            else:
                f["buyers"] = rec["buyers"]
            f["occasions_per_buyer"] = rec["occasions"] / rec["buyers"]
            f["units_per_occasion"] = rec["units"] / rec["occasions"]
            return f

        fb, fc = factors(pair["base"]), factors(pair["current"])
        effects = shapley_multiplicative(fb, fc)
        change = pair["current"]["units"] - pair["base"]["units"]
        rec = reconcile(change, effects, args.tolerance)
        results[segment] = {
            "window": pair["base"]["window"],
            "base": {k: to_float(v) for k, v in fb.items()},
            "current": {k: to_float(v) for k, v in fc.items()},
            "base_buyers": to_float(pair["base"]["buyers"]),
            "current_buyers": to_float(pair["current"]["buyers"]),
            "base_volume": to_float(pair["base"]["units"]),
            "current_volume": to_float(pair["current"]["units"]),
            "volume_change": to_float(change),
            "volume_growth_pct": pct(change, pair["base"]["units"]),
            "penetration_pct": {"base": to_float(fb["penetration"] * 100, 6), "current": to_float(fc["penetration"] * 100, 6)} if "penetration" in fb else None,
            "penetration_note": None if "penetration" in fb else "not computed: no eligible population supplied",
            "effects": {k: to_float(v) for k, v in effects.items()},
            "reconciliation": rec,
        }

    notes = []
    if args.segment_col and len(results) > 1:
        notes.append("Segments are decomposed separately. Buyers may overlap across segments, so segment buyer counts are not summed.")
    return {
        "recipe": "buyers",
        "status": "ok",
        "convention": {
            "identity": "volume = eligible population x penetration x occasions per buyer x units per occasion" if args.population_col else "volume = buyers x occasions per buyer x units per occasion",
            "attribution": "Shapley (average of all factor orderings): order-independent and exact",
            "window": "both periods must share the same window",
            "form": "rates" if rates_form else "counts",
        },
        "results": results,
        "warnings": notes,
        "interpretation_limits": [
            "Attribution shows which multiplicative component moved volume. It does not explain why buyers or frequency changed.",
            "Penetration is only as valid as the eligible population definition; panel or survey estimates carry sampling error not shown here.",
        ],
        "provenance": provenance(args, args.input, len(rows), len(scoped)),
    }


# ---------------------------------------------------------------------------
# contribution
# ---------------------------------------------------------------------------

def run_contribution(args):
    fieldnames, rows = read_csv(args.input)
    require_columns(fieldnames, [args.period_col, args.group_col, args.value_col, args.unit_col, args.measure_col, args.definition_col, args.market_total_col])
    check_periods(rows, args.period_col, args.base, args.current)
    scoped = [r for r in rows if r[args.period_col] in (args.base, args.current)]
    missing = [r["__line__"] for r in scoped if is_missing(r.get(args.value_col))]
    if missing:
        raise DataContractError("MISSING_VALUES", "Missing values in the value column; unknown is not zero.", {"lines": missing[:100]})
    unit = single_value(scoped, args.unit_col, "MIXED_UNITS", "unit")
    measure = single_value(scoped, args.measure_col, "MIXED_MEASURES", "measure (e.g. value vs volume)")
    if args.definition_col:
        definitions = {(r[args.period_col], r[args.definition_col]) for r in scoped}
        per_period = {}
        for period, definition in definitions:
            per_period.setdefault(period, set()).add(definition)
        if any(len(v) > 1 for v in per_period.values()) or len({next(iter(v)) for v in per_period.values()}) > 1:
            raise DataContractError("DEFINITION_CHANGED", "Market or category definition differs within or between periods; shares and contributions are not comparable.", {"definitions": {k: sorted(v) for k, v in per_period.items()}})

    values = {}
    totals_declared = {}
    for r in scoped:
        key = (r[args.group_col], r[args.period_col])
        if key in values:
            raise DataContractError("DUPLICATE_GRAIN", "More than one row per group and period.", {"group": key[0], "period": key[1]})
        v = parse_number(r[args.value_col], args.value_col, r["__line__"])
        if v < 0 and not args.allow_negative:
            raise DataContractError("NEGATIVE_VALUES", "Negative value. Pass --allow-negative only for measures that can legitimately be negative (e.g. profit).", {"line": r["__line__"]})
        values[key] = v
        if args.market_total_col:
            if is_missing(r.get(args.market_total_col)):
                raise DataContractError("MISSING_VALUES", "Missing market total.", {"line": r["__line__"]})
            t = parse_number(r[args.market_total_col], args.market_total_col, r["__line__"])
            previous = totals_declared.setdefault(r[args.period_col], t)
            if previous != t:
                raise DataContractError("INCONSISTENT_DENOMINATOR", "Market total differs between rows of the same period.", {"period": r[args.period_col]})

    groups = sorted({k[0] for k in values})
    absent_base = [g for g in groups if (g, args.base) not in values]
    absent_current = [g for g in groups if (g, args.current) not in values]
    zero = Fraction(0)
    sum_base = sum((values.get((g, args.base), zero) for g in groups), zero)
    sum_current = sum((values.get((g, args.current), zero) for g in groups), zero)

    denominators = {"base": sum_base, "current": sum_current}
    unallocated = None
    if args.market_total_col:
        for label, period, s in (("base", args.base, sum_base), ("current", args.current, sum_current)):
            total = totals_declared[period]
            if s - total > Fraction(Decimal(str(args.tolerance))):
                raise DataContractError("SHARE_EXCEEDS_TOTAL", "Groups sum to more than the declared market total; definitions or units are inconsistent.", {"period": period, "sum_of_groups": to_float(s), "market_total": to_float(total)})
            denominators[label] = total
        unallocated = {"base": to_float(denominators["base"] - sum_base), "current": to_float(denominators["current"] - sum_current)}

    total_change = denominators["current"] - denominators["base"]
    rows_out = []
    components = {}
    for g in groups:
        b = values.get((g, args.base), zero)
        c = values.get((g, args.current), zero)
        delta = c - b
        components[g] = delta
        rows_out.append({
            "group": g,
            "base": to_float(b),
            "current": to_float(c),
            "change": to_float(delta),
            "growth_pct": pct(delta, b) if b else None,
            "growth_note": None if b else "not computed: zero or absent base",
            "contribution_to_total_growth_pp": pct(delta, denominators["base"]),
            "share_of_total_change_pct": pct(delta, total_change) if total_change else None,
            "share_base_pct": pct(b, denominators["base"]),
            "share_current_pct": pct(c, denominators["current"]),
            "share_change_pp": round(pct(c, denominators["current"]) - pct(b, denominators["base"]), 6) if denominators["base"] and denominators["current"] else None,
        })
    if unallocated is not None:
        components["__unallocated__"] = (denominators["current"] - sum_current) - (denominators["base"] - sum_base)
    rec = reconcile(total_change, components, args.tolerance)

    flags = []
    if absent_base or absent_current:
        flags.append("Some groups are absent in one period and are treated as zero there; check whether this is real entry/exit or missing data.")
    if args.focus_group:
        focus = next((r for r in rows_out if r["group"] == args.focus_group), None)
        if focus is None:
            raise DataContractError("GROUP_NOT_FOUND", "Focus group not found.", {"focus_group": args.focus_group})
        if focus["growth_pct"] is not None and pct(total_change, denominators["base"]) is not None:
            market_growth = pct(total_change, denominators["base"])
            if focus["growth_pct"] < market_growth:
                flags.append("{} grew {:.2f}% versus total {:.2f}%: absolute growth with share loss.".format(args.focus_group, focus["growth_pct"], market_growth))
            elif focus["growth_pct"] > market_growth:
                flags.append("{} grew faster than the total ({:.2f}% vs {:.2f}%): share gain.".format(args.focus_group, focus["growth_pct"], market_growth))
    return {
        "recipe": "contribution",
        "status": "ok",
        "convention": {
            "denominator": "declared market total per period" if args.market_total_col else "sum of groups per period",
            "contribution_to_total_growth_pp": "group change / base-period denominator x 100",
            "share_of_total_change_pct": "group change / total change x 100 (not computed when total change is zero)",
            "absent_groups": "treated as zero in the period where absent and listed",
            "unit": unit,
            "measure": measure,
        },
        "results": {
            "base_period": args.base,
            "current_period": args.current,
            "base_total": to_float(denominators["base"]),
            "current_total": to_float(denominators["current"]),
            "total_change": to_float(total_change),
            "total_growth_pct": pct(total_change, denominators["base"]),
            "unallocated": unallocated,
            "groups_absent_in_base": absent_base,
            "groups_absent_in_current": absent_current,
            "groups": rows_out,
        },
        "reconciliation": rec,
        "flags": flags,
        "warnings": [] if args.market_total_col or args.complete_market else ["Shares use the sum of supplied groups as the denominator. If the groups do not cover the whole market, these are shares of the supplied set, not market shares."],
        "interpretation_limits": ["Contribution shows where change arose among groups sharing one denominator and unit; it does not establish cause."],
        "provenance": provenance(args, args.input, len(rows), len(scoped)),
    }


# ---------------------------------------------------------------------------
# join-check
# ---------------------------------------------------------------------------

def run_join_check(args):
    left_fields, left = read_csv(args.left)
    right_fields, right = read_csv(args.right)
    keys = split_cols(args.on)
    require_columns(left_fields, keys)
    require_columns(right_fields, keys)
    def index(rows):
        idx = {}
        for r in rows:
            idx.setdefault(tuple(r[k] for k in keys), []).append(r["__line__"])
        return idx
    li, ri = index(left), index(right)
    right_dups = {k: v for k, v in ri.items() if len(v) > 1}
    if right_dups and not args.allow_many:
        raise DataContractError("JOIN_FANOUT", "Right table has duplicate join keys; joining would multiply left rows and inflate totals.", {"keys": keys, "duplicates": [{"key": list(k), "lines": v} for k, v in list(right_dups.items())[:50]]})
    left_only = sorted(set(li) - set(ri))
    right_only = sorted(set(ri) - set(li))
    if (left_only or right_only) and args.require_complete:
        raise DataContractError("JOIN_INCOMPLETE", "Keys do not match completely between tables.", {"left_only": [list(k) for k in left_only[:50]], "right_only": [list(k) for k in right_only[:50]]})
    return {
        "recipe": "join-check",
        "status": "ok",
        "results": {
            "keys": keys,
            "left_rows": len(left),
            "right_rows": len(right),
            "matched_keys": len(set(li) & set(ri)),
            "left_only_keys": [list(k) for k in left_only[:50]],
            "left_only_count": len(left_only),
            "right_only_keys": [list(k) for k in right_only[:50]],
            "right_only_count": len(right_only),
            "right_duplicate_key_count": len(right_dups),
        },
        "warnings": ["Unmatched keys would become missing values after a left join; decide explicitly how to treat them."] if left_only else [],
        "interpretation_limits": ["Key coverage does not prove the two tables share definitions, periods or units."],
        "provenance": {"left": args.left, "right": args.right, "left_sha256": file_sha256(args.left), "right_sha256": file_sha256(args.right), "script_version": SCRIPT_VERSION},
    }


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def markdown_summary(result):
    lines = ["# {} result".format(result["recipe"]), ""]
    if result["recipe"] == "pvm":
        r = result["results"]
        lines += ["Revenue {} → {} ({}): change {} ({}%).".format(r["base_revenue"], r["current_revenue"], result["convention"]["currency"] or "currency not declared", r["revenue_change"], r["revenue_growth_pct"]), "", "| Component | Value |", "|---|---|"]
        lines += ["| {} | {} |".format(k, v) for k, v in r["components"].items()]
    elif result["recipe"] == "buyers":
        for segment, r in result["results"].items():
            lines += ["## {}".format(segment), "", "| Effect | Units |", "|---|---|"] + ["| {} | {} |".format(k, v) for k, v in r["effects"].items()] + [""]
    elif result["recipe"] == "contribution":
        lines += ["| Group | Base | Current | Contribution (pp) | Share change (pp) |", "|---|---|---|---|---|"]
        lines += ["| {group} | {base} | {current} | {contribution_to_total_growth_pp} | {share_change_pp} |".format(**g) for g in result["results"]["groups"]]
    if "reconciliation" in result:
        rec = result["reconciliation"]
        lines += ["", "Reconciles: {} (residual {}, tolerance {}).".format(rec["reconciles"], rec["residual"], rec["tolerance"])]
    for heading, key in (("Flags", "flags"), ("Warnings", "warnings"), ("Limits", "interpretation_limits")):
        if result.get(key):
            lines += ["", "**{}**".format(heading)] + ["- " + item for item in result[key]]
    return "\n".join(lines)


def build_parser():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="recipe")

    def common(p):
        p.add_argument("--format", choices=["json", "md"], default="json")
        p.add_argument("--output", help="write result to this file instead of stdout")

    p = sub.add_parser("profile", help="profile a CSV file")
    p.add_argument("--input", required=True)
    p.add_argument("--grain", help="comma-separated columns that should uniquely identify a row")
    p.add_argument("--key-col")
    p.add_argument("--unit-col")
    p.add_argument("--period-col")
    common(p)
    p.set_defaults(func=run_profile)

    p = sub.add_parser("pvm", help="price-volume-mix revenue bridge")
    p.add_argument("--input", required=True)
    p.add_argument("--key", required=True, help="item column, e.g. sku")
    p.add_argument("--period-col", required=True)
    p.add_argument("--base", required=True)
    p.add_argument("--current", required=True)
    p.add_argument("--quantity-col", required=True)
    p.add_argument("--revenue-col")
    p.add_argument("--price-col")
    p.add_argument("--unit-col")
    p.add_argument("--currency-col")
    p.add_argument("--dims", help="extra grain columns, e.g. region,channel")
    p.add_argument("--period-days-col")
    p.add_argument("--allow-unequal-periods", action="store_true")
    p.add_argument("--interaction", choices=["allocate-to-price", "separate"], default="allocate-to-price")
    p.add_argument("--revenue-basis", choices=["gross", "net", "unknown"], default="unknown")
    p.add_argument("--exclude-missing", action="store_true")
    p.add_argument("--tolerance", type=float, default=0.01)
    common(p)
    p.set_defaults(func=run_pvm)

    p = sub.add_parser("buyers", help="buyers x frequency x units decomposition")
    p.add_argument("--input", required=True)
    p.add_argument("--period-col", required=True)
    p.add_argument("--base", required=True)
    p.add_argument("--current", required=True)
    p.add_argument("--buyers-col", required=True)
    p.add_argument("--occasions-col")
    p.add_argument("--units-col")
    p.add_argument("--frequency-col")
    p.add_argument("--units-per-occasion-col")
    p.add_argument("--volume-col")
    p.add_argument("--population-col")
    p.add_argument("--window-col")
    p.add_argument("--segment-col")
    p.add_argument("--tolerance", type=float, default=0.000001)
    common(p)
    p.set_defaults(func=run_buyers)

    p = sub.add_parser("contribution", help="contribution to change and shares by group")
    p.add_argument("--input", required=True)
    p.add_argument("--period-col", required=True)
    p.add_argument("--base", required=True)
    p.add_argument("--current", required=True)
    p.add_argument("--group-col", required=True)
    p.add_argument("--value-col", required=True)
    p.add_argument("--unit-col")
    p.add_argument("--measure-col")
    p.add_argument("--definition-col")
    p.add_argument("--market-total-col")
    p.add_argument("--complete-market", action="store_true", help="declare that the groups cover the whole market")
    p.add_argument("--focus-group")
    p.add_argument("--allow-negative", action="store_true")
    p.add_argument("--tolerance", type=float, default=0.01)
    common(p)
    p.set_defaults(func=run_contribution)

    p = sub.add_parser("join-check", help="check key coverage and fan-out before a join")
    p.add_argument("--left", required=True)
    p.add_argument("--right", required=True)
    p.add_argument("--on", required=True)
    p.add_argument("--allow-many", action="store_true")
    p.add_argument("--require-complete", action="store_true")
    common(p)
    p.set_defaults(func=run_join_check)
    return parser


def main(argv=None):
    parser = build_parser()
    args = parser.parse_args(argv)
    if not getattr(args, "func", None):
        parser.print_help()
        return 1
    try:
        result = args.func(args)
        code = 0
    except DataContractError as error:
        result = {"recipe": args.recipe, "status": "error", "code": error.code, "message": error.message, "details": error.details}
        code = 2
    text = markdown_summary(result) if args.format == "md" and result["status"] == "ok" else json.dumps(result, indent=2, ensure_ascii=False)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as handle:
            handle.write(text + "\n")
    else:
        print(text)
    return code


if __name__ == "__main__":
    sys.exit(main())
