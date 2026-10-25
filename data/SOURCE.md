# Source and transformation

Moro, S., Rita, P., & Cortez, P. (2014). *Bank Marketing* [Dataset]. UCI Machine Learning Repository. [DOI 10.24432/C5K306](https://doi.org/10.24432/C5K306). The UCI dataset is published under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Official dataset: https://archive.ics.uci.edu/dataset/222/bank+marketing

Original source ZIP: https://archive.ics.uci.edu/static/public/222/bank+marketing.zip. This project uses `bank.zip/bank-full.csv` (45,211 records, 17 fields) and preserves the original `bank-names.txt`. The adapted `campaigns.csv` has one source record per row, labels selected categories, adds the binary `Subscribed` and constant `Records`, and groups contact counts into explicit bands. Source and transformation checks are in `scripts/analyze.py`.

Source CSV SHA-256: `d1513ec63b385506f7cfce9f2c5caa9fe99e7ba4e8c3fa264b3aaf0f849ed32d`.

The original file is ordered by date but includes only month and day, no calendar year. Month comparisons pool multiple years; they are not a valid continuous monthly time series. `Unknown` is a source category rather than a missing value that we impute. There is no campaign spend, revenue, random assignment, or unique customer identifier. A row is a source record tied to the last contact and outcome, not a count of individual calls.
