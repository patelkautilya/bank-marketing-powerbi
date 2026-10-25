# Findings | Bank marketing campaign analysis

## Executive readout

The source contains **45,211 campaign records** and **5,289 term-deposit subscriptions**, an observed **11.70% subscription rate**. The recorded current-campaign contact counts sum to **124,956** (2.76 per record). The analysis is historical, descriptive, and based on UCI's legacy `bank-full.csv`.

## What the segments show

- **Contact channel:** cellular has 4,369 subscriptions across 29,285 records (**14.92%**); telephone has 390 / 2,906 (**13.42%**). The `Unknown` channel has 530 / 13,020 (**4.07%**). Data quality and period mix need investigation before a channel decision.
- **Repeated contacts:** records with one current-campaign contact show 2,561 / 17,544 subscriptions (**14.60%**); records with 11 or more show 47 / 1,196 (**3.93%**). This pattern is consistent with harder cases receiving more follow-up and does not demonstrate that contacts reduce conversion.
- **Prior campaign outcome:** `Success` has 978 / 1,511 subscriptions (**64.73%**), versus `Unknown` 3,386 / 36,959 (**9.16%**). The groups differ strongly in history and size; these are descriptive cohorts, not a prospective targeting policy.
- **Housing-loan flag:** the `No` group records 3,354 / 20,081 subscriptions (**16.70%**), while `Yes` records 1,935 / 25,130 (**7.70%**). This is a sensitive credit-related attribute; the comparison is presented for descriptive completeness and should not be used alone for outreach or eligibility decisions.

## Reporting and proposed follow-up

Reconcile `Unknown` channel labels with data collection, obtain a year/campaign identifier and exact contact timestamps, and add spend and revenue before considering efficiency or ROI. Use an appropriate experimental or carefully adjusted study before changing an outreach policy. Report cohort sizes next to percentages; several high-rate months have far fewer records than May.

The original file provides month and day but no year. A month visual pools years, so it does not show growth or seasonality in a single complete calendar series. Campaign-contact counts are already aggregated by record. A sum is not a verified count of unique calls. Subscription is an observed outcome, not revenue.

## Validation

`scripts/analyze.py` downloads the original UCI archive, checks shape, categories, nulls and contact-count domain, derives the reporting file, computes segment summaries and independently reconciles totals in SQLite. Power BI measures must equal the 45,211 / 5,289 / 11.70% source baseline and update under filters.
