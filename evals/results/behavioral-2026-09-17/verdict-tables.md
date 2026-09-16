## Run 1 (skill as first built)
| Case | Tier | Baseline verdict | Skill verdict | Baseline correction | Skill correction | Unsupported claims (base / skill) | Words (base / skill) | Judge preferred |
|---|---|---|---|---|---|---|---|---|
| BEH-01 | standard | PASS | PASS | light | light | 7 / 4 | 1778 / 2522 | treatment |
| BEH-02 | standard | PASS | PASS | light | light | 3 / 1 | 1057 / 1457 | treatment |
| BEH-05 | adversarial | PASS | PASS | light | light | 4 / 2 | 1127 / 1412 | treatment |
| BEH-06 | adversarial | FAIL | PASS | substantial | light | 10 / 4 | 3064 / 2405 | treatment |
| BEH-08 | standard | PASS | PASS | light | light | 3 / 5 | 680 / 683 | treatment |
| BEH-12 | standard | PASS | PASS | light | none | 7 / 1 | 1061 / 1440 | treatment |
| BEH-13 | standard | PASS | PASS | light | light | 5 / 2 | 2083 / 2392 | baseline |
| BEH-16 | adversarial | PASS | PASS | light | light | 5 / 2 | 1121 / 1783 | treatment |
| BEH-17 | ambiguous | PASS | PASS | light | light | 3 / 2 | 1414 / 3215 | baseline |
| BEH-20 | standard | PASS | PASS | none | none | 1 / 1 | 85 / 91 | baseline |
| BEH-22 | adversarial | PASS | PASS | light | light | 5 / 2 | 951 / 1381 | treatment |
| BEH-25 | ambiguous | PASS | PASS | light | light | 3 / 2 | 797 / 936 | treatment |
| HELDOUT-01 | adversarial (held-out) | PASS | PASS | light | light | 3 / 0 | 498 / 669 | treatment |
| HELDOUT-02 | standard (held-out) | PASS | PASS | light | light | 5 / 2 | 1259 / 1144 | treatment |

## Run 2 (after output-shaping repair; skill re-run on five cases, compared with the same baseline answers)
| Case | Tier | Baseline verdict | Skill verdict | Baseline correction | Skill correction | Unsupported claims (base / skill) | Words (base / skill) | Judge preferred |
|---|---|---|---|---|---|---|---|---|
| BEH-02 | standard | PASS | PASS | light | light | 4 / 1 | 1057 / 1076 | baseline |
| BEH-06 | adversarial | PASS | PASS | substantial | light | 10 / 4 | 3064 / 1966 | treatment |
| BEH-13 | standard | PASS | PASS | light | light | 4 / 0 | 2083 / 1993 | baseline |
| BEH-16 | adversarial | PASS | PASS | light | light | 5 / 2 | 1121 / 1481 | treatment |
| BEH-17 | ambiguous | PASS | PASS | light | light | 2 / 1 | 1414 / 1924 | treatment |
