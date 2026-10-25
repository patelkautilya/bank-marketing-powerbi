# Campaign performance brief

**Audience:** marketing operations and analytics teams reviewing a historical Portuguese bank term-deposit calling dataset.

**Decision supported:** where to investigate contact mix, repeated outreach, and recorded prior campaign outcomes. This report describes historical associations; it does not optimize targeting or predict customer behavior.

**Unit of analysis:** one row in UCI `bank-full.csv`, containing details of the last contact, total contacts in the current campaign for that record, a prior campaign outcome, and whether a term deposit was subscribed. The source does not provide a unique customer key or campaign spend.

**KPI definitions:**

| KPI | Definition | All records |
| --- | --- | ---: |
| Campaign records | Sum of constant `Records=1` | 45,211 |
| Subscriptions | Sum of `Subscribed=1` | 5,289 |
| Subscription rate | Subscriptions / campaign records | 11.70% |
| Contacts per record | Sum of reported current-campaign contact counts / records | 2.76 |

All rates are recalculated from counts within the active filter context. Do not average precomputed segment rates.

**Important limits:** the source supplies contact month and day but no calendar year, so monthly comparisons pool years and are not a time series. `Unknown` in contact channel or prior outcome is a recorded category. There is no expense or revenue, so ROI and profitability cannot be calculated. The contact count and prior outcome could be related to selection into outreach; observed rate gaps cannot be attributed causally to a channel or number of attempts. Job and education fields are retained to document the source but not used for targeting recommendations. Do not interpret a source record as one unique person or one call.
