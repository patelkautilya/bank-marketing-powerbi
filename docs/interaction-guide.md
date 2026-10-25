# Power BI interaction guide

Open the [live report](https://app.powerbi.com/groups/e6426da3-9b36-4519-acf1-2434daa552ae/reports/87434d11-5167-448c-ada3-35df94db0b8e/333e319908aed0f37c63?experience=power-bi) while signed in to Power BI, or download the [editable PBIX](../reports/bank-marketing.pbix) to explore it locally.

| Page | Interaction | What to inspect |
| --- | --- | --- |
| 01 Campaign Overview | Select a contact channel bar or a month in the combination chart. | The KPI cards and other visuals cross-filter. Select the same data point again to clear the selection. |
| 02 Contact Strategy | Select a contact-count band in the bar chart or a matrix cell. | The KPI cards recalculate for the selected cohort. For example, selecting **1 contact** displays roughly 18K records, 3K subscriptions and **14.60%**. |
| 03 Prior Outcome | Select an outcome/channel bar or a donut segment. | Compare the rate within a cohort against its share of all subscriptions. The grouped bars encode contact channel with distinct colors. |

Use **Default Values** when exporting all report pages to PDF. The [portfolio PDF](../reports/bank-marketing.pdf) and [dashboard images](../visuals/dashboard-1.png) show the unfiltered baseline. A separate [live KPI dashboard](https://app.powerbi.com/groups/e6426da3-9b36-4519-acf1-2434daa552ae/dashboards/66ee6b6f-d506-4384-aed0-5f7c8c42f142?experience=power-bi) pins the overview page. Power BI access to the live report and dashboard may require the owner's workspace permissions; the PBIX, PDF, and PNGs are public in this repository.

The source records have month/day but no year. Month selection pools multiple years and must not be interpreted as a time-series growth pattern. The report is descriptive; selections do not imply a causal channel or contact-frequency effect.
