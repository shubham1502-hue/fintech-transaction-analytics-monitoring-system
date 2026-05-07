# Fintech Transaction Monitoring System

Transaction monitoring workflow for failed GMV, payment reliability, SQL diagnostics, risk signals, and BI-ready outputs.

<!-- FOUNDER_OS_STANDARD_README -->

## The founder problem

Payment systems can process volume while still leaking revenue through preventable failures, bank or provider issues, peak-hour reliability problems, and risk signals. Founders need to know where reliability is breaking and what to investigate first.

## What this repo does

- generates synthetic transaction data
- cleans and validates transaction outputs
- runs SQL-style analytics modules
- supports optional MySQL export
- documents Tableau-ready dashboard structure

## What a founder gets in 10 minutes

- raw and clean transaction samples
- validation notes
- SQL diagnostics
- dashboard preview
- data dictionary

## Before and after

Before:

- transaction failures buried in exports
- no failure-rate narrative
- manual SQL investigation
- unclear merchant or provider risk

After:

- clean monitoring dataset
- reliability diagnostics
- risk segmentation
- BI-ready outputs
- database export path

## Who this is for

- fintech founders
- payments operators
- data analysts
- Founder's Office teams
- BizOps operators

## Quick start

- Run `python3 -m pip install -r requirements.txt`.
- Run `python3 src/generate_dataset.py`.
- Run `python3 src/dataset_validation.py`.
- Or run `sh run_pipeline.sh`.
- Open `docs/project_walkthrough.md` and `dashboard/screenshots/fintech_dashboard_preview.png` first.

## How to fork and use this for your company

1. Click Fork.
2. Rename the repo if needed.
3. Replace sample files under `data/raw/` and `data/processed/` with private local exports.
4. Keep MySQL credentials in environment variables using `.env.example` as a guide.
5. Run validation before trusting any analysis.
6. Move outputs into Tableau, Power BI, Mode, Hex, or an internal monitoring tracker.

### Non-technical path

- Replace one dataset in `data/raw/`.
- Edit one `.env` locally only if using MySQL.
- Run `sh run_pipeline.sh`.
- Read one output first: `docs/project_walkthrough.md`.

## Input format

- transaction ID
- merchant
- customer or account identifier
- amount
- status
- failure reason
- bank or provider
- country
- timestamp
- risk signals

The default sample data and examples are synthetic, anonymized, or template-only unless the repo explicitly documents a public source. Keep private customer, prospect, employee, investor, borrower, merchant, payment, or company data out of public forks.

## Output files

- `data/raw/transactions_raw_sample.csv`: synthetic raw sample
- `data/processed/transactions_clean_sample.csv`: clean sample
- `docs/data_dictionary.md`: field guide
- `docs/project_walkthrough.md`: operating walkthrough
- `dashboard/screenshots/fintech_dashboard_preview.png`: dashboard preview
- `sql/`: analysis modules

## Example founder workflow

- Monday: refresh transaction extract.
- Tuesday: run validation.
- Wednesday: inspect failed GMV and reliability drivers.
- Thursday: assign provider, bank, or merchant follow-up.
- Friday: summarize risks in the payments review.

## Customization guide

Customize these before using the repo for a real company:

- failure categories
- risk thresholds
- merchant segments
- SQL questions
- database connection
- dashboard fields

## Where this fits in the Founder OS

Use this with `payments-business-management` for business review and `payments-monitoring-fraud-detection` for anomaly and fraud-style monitoring.

## Why this matters

This is not only transaction analytics. It is a reliability workflow for finding preventable payment leakage.

## Roadmap

- streaming alert prototype
- Slack alerts
- processor import templates
- Tableau packaged workbook
- weekly payments review integration

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) if present. Practical improvements are welcome when they make the workflow easier to fork, run, or adapt.

## License

MIT License. See [LICENSE](LICENSE).

## Built by

Built by Shubham Singh, a founder-facing operator focused on RevOps, GTM systems, startup metrics, AI workflows, and operating systems for early-stage teams.

## Use this in your company

Fork it, replace the sample inputs with your company context, and run the workflow. Start with the main output listed in the Quick Start section. Keep private data out of public forks.

## If you are a Founder's Office candidate

Use this repo to understand how a founder-facing operator turns messy inputs into decisions, cadence, and execution artifacts. Fork it, adapt it to a real company example, and write a short case note explaining what changed.

---

## Detailed implementation notes

The founder-facing guide above is the fastest path. The original repo-specific notes are preserved below for deeper implementation context.

Fintech transaction monitoring system for failed GMV, payment reliability, SQL diagnostics, risk signals, and Tableau analytics.

Fintech teams lose revenue and user trust when failed transactions, bank/provider issues, merchant concentration, peak-hour reliability problems, and risk signals are not visible quickly. This repo models a transaction-level monitoring workflow for diagnosing payment failures, identifying reliability hot spots, and supporting SQL-driven product/data investigations.

## Problem

Payment systems can process high transaction volume while still leaking revenue through preventable failures. The operating problem is not only "what is the success rate?" It is:

- Which failures are driving failed GMV?
- Which banks or payment methods are unreliable?
- Which merchants create concentrated transaction or failure risk?
- When do failures spike during the day?
- Which users show suspicious high-value or repeated-failure behavior?

This project focuses on transaction-level reliability and risk diagnostics, not monthly portfolio management.

## What This Repo Includes

- `src/generate_dataset.py`: synthetic transaction generator for 50,000 payment transactions.
- `src/dataset_validation.py`: validation and diagnostic script for failure rate, unexplained failures, merchant concentration, peak-hour reliability, bank variance, and fraud flags.
- `src/python_export.py`: optional MySQL export helper that reads a `transactions` table and writes `data/processed/transactions_clean.csv`.
- `src/generate_sample_data.py`: utility for sampling full raw/processed datasets into portfolio-safe sample CSVs.
- `sql/eda_queries.sql`: baseline transaction exploration.
- `sql/kpi_queries.sql`: GMV, failed GMV, success rate, and transaction volume queries.
- `sql/risk_analysis.sql`: merchant, bank, payment-method, and high-risk-user diagnostics.
- `sql/advanced_analysis.sql`: hourly failure trends, merchant Pareto analysis, and failure reason contribution.
- `sql/business_questions.sql`: product/operator questions for bank, payment method, and suspicious user investigation.
- `data/raw/transactions_raw_sample.csv`: tracked sample raw transaction dataset.
- `data/processed/transactions_clean_sample.csv`: tracked sample processed transaction dataset.
- `dashboard/screenshots/fintech_dashboard_preview.png`: Tableau dashboard preview.
- `docs/`: data dictionary, data note, and project walkthrough.

Full generated datasets are ignored by Git and kept local.

## How This Differs From My Payments Business Management Repo

This repo is the transaction-level reliability and risk diagnostics layer.

`payments-business-management` is the monthly business management pack: merchant portfolio KPIs, regional contribution, budget variance, SLA risk, and executive reporting.

Use this repo when the question is:

- "Why are transactions failing?"
- "Which provider, bank, merchant, hour, or user pattern needs investigation?"
- "Where is failed GMV coming from?"

Use the payments business management repo when the question is:

- "How is the payments business performing this month?"
- "Which merchants, regions, or budget lines need executive attention?"
- "What should go into the management pack?"

## System Workflow

1. Generate or ingest transaction-level payment data.
2. Validate the dataset and inspect failure, merchant, bank, peak-hour, and fraud indicators.
3. Export or load clean transaction data into a SQL environment.
4. Run SQL modules for KPIs, reliability diagnostics, risk segmentation, and business questions.
5. Use Tableau to explore failed GMV, success rate, risk patterns, bank variance, and merchant concentration.
6. Convert the diagnostic output into product, payments ops, or risk follow-up actions.

## KPI And Diagnostic Logic

Core KPIs:

- Total GMV = sum of transaction amount.
- Failed GMV = transaction amount where status is `FAILED`.
- Success rate = successful transactions / total transactions.
- Total transactions = transaction count.

Diagnostic logic:

- Failure reason mix identifies system, bank, timeout, insufficient funds, and fraud-suspected patterns.
- Merchant concentration highlights whether a small set of merchants drives failed GMV.
- Peak-hour failure rate compares evening traffic windows against the overall failure rate.
- Bank variance isolates issuing banks with higher failure rates.
- Payment-method variance compares reliability across UPI, card, and wallet.
- High-risk user logic flags repeated high-value or suspicious transaction behavior.

The current sample data is synthetic and includes simulated failure clustering, peak-hour reliability issues, bank-specific failure variation, and risk flags.

## SQL Analysis Modules

- `sql/eda_queries.sql`: counts, status distribution, and failure reason exploration.
- `sql/kpi_queries.sql`: total GMV, failed GMV, success rate, and transaction count.
- `sql/risk_analysis.sql`: merchant failed GMV, bank failure rate, payment-method failure rate, and high-risk users.
- `sql/advanced_analysis.sql`: hourly failure trend, merchant Pareto view, and failure reason contribution percentage.
- `sql/business_questions.sql`: practical investigation queries for failed GMV by bank, unreliable payment methods, and abnormal users.

These queries assume a SQL table or view named `transactions_clean`.

## Example Product/Data Use Cases

- Payments reliability review: find the highest failed-GMV drivers before an incident review.
- Product analytics: quantify whether failures are caused by banks, payment methods, merchants, or peak-hour load.
- Risk operations: identify users with repeated high-value or abnormal transaction patterns.
- Merchant operations: prioritize merchant follow-up when failed GMV is concentrated.
- Engineering triage: identify unexplained failures or bank/provider variance that needs deeper system logs.
- Tableau reporting: create a transaction monitoring layer for product, ops, and risk teams.

## Use This In Your Company

1. Replace the synthetic sample with sanitized processor, PSP, bank, or internal transaction exports.
2. Map your transaction schema to amount, status, timestamp, merchant, payment method, issuing bank, failure reason, and user ID.
3. Run the validation script to check failure rates, unexplained failures, merchant concentration, peak-hour spikes, and bank variance.
4. Load processed transactions into your SQL warehouse or local database as `transactions_clean`.
5. Tune SQL thresholds for your own failure, GMV, risk, and anomaly tolerance.
6. Refresh the Tableau dashboard or connect the same outputs to your BI tool.
7. Review diagnostics weekly with product, payments ops, risk, and engineering owners.

## Minimum Edits Before First Use

| Edit | Where | Why |
| --- | --- | --- |
| Map transaction schema | `docs/data_dictionary.md` and source data | Align status, amount, timestamp, merchant, bank, payment method, and user fields. |
| Replace synthetic data | `data/raw/transactions_raw.csv` or your warehouse export | Use real sanitized payment data before making operating decisions. |
| Tune validation checks | `src/dataset_validation.py` | Match your normal failure rate, peak-hour window, merchant concentration threshold, and fraud assumptions. |
| Configure optional database export | `.env.example` and `src/python_export.py` | Keep database credentials in environment variables and export clean data to `data/processed/`. |
| Adapt SQL modules | `sql/*.sql` | Match your SQL dialect, table name, risk thresholds, and product questions. |
| Update dashboard labels | Tableau dashboard and `docs/project_walkthrough.md` | Reflect your payment methods, providers, regions, and investigation workflow. |

## How To Run / Use

Install dependencies:

```bash
python3 -m pip install -r requirements.txt
```

Generate the full synthetic raw dataset:

```bash
python3 src/generate_dataset.py
```

Validate transaction diagnostics:

```bash
python3 src/dataset_validation.py
```

Or run both steps:

```bash
sh run_pipeline.sh
```

Optional MySQL export:

```bash
cp .env.example .env
# Fill MYSQL_* values locally, then run:
python3 src/python_export.py
```

The optional export expects a MySQL table named `transactions` and writes `data/processed/transactions_clean.csv`.

## Outputs

Tracked portfolio outputs:

- `data/raw/transactions_raw_sample.csv`: sample raw transaction export.
- `data/processed/transactions_clean_sample.csv`: sample processed transaction export.
- `dashboard/screenshots/fintech_dashboard_preview.png`: Tableau dashboard screenshot.
- `docs/project_walkthrough.md`: project rationale, approach, insights, and next steps.

Local generated outputs:

- `data/raw/transactions_raw.csv`: full synthetic dataset generated by `src/generate_dataset.py`.
- `data/processed/transactions_clean.csv`: optional processed export from MySQL.

The full generated CSVs are ignored so they do not get staged accidentally.

## Dashboard

![Fintech transaction dashboard](dashboard/screenshots/fintech_dashboard_preview.png)

Interactive Tableau dashboard:
[Payments Transactions Analytics Monitoring](https://public.tableau.com/views/PaymentsTransactionsAnalyticsMonitoring/Dashboard1)

The dashboard is used for failed GMV monitoring, success-rate visibility, failure diagnostics, bank/payment-method variance, merchant concentration, and risk-pattern exploration.

## Folder Structure

```text
.
|-- dashboard/
|  `-- screenshots/
|    `-- fintech_dashboard_preview.png
|-- data/
|  |-- processed/
|  |  `-- transactions_clean_sample.csv
|  `-- raw/
|    `-- transactions_raw_sample.csv
|-- docs/
|  |-- data_dictionary.md
|  |-- data_note.md
|  `-- project_walkthrough.md
|-- sql/
|  |-- advanced_analysis.sql
|  |-- business_questions.sql
|  |-- eda_queries.sql
|  |-- kpi_queries.sql
|  `-- risk_analysis.sql
|-- src/
|  |-- dataset_validation.py
|  |-- generate_dataset.py
|  |-- generate_sample_data.py
|  `-- python_export.py
|-- .env.example
|-- .gitignore
|-- LICENSE
|-- README.md
|-- requirements.txt
`-- run_pipeline.sh
```

## Customization Guide

- For PSP reliability: add provider, gateway, acquirer, decline code, and retry outcome fields.
- For bank reliability: add issuer response code, bank outage flags, and downtime windows.
- For merchant concentration: add merchant category, settlement region, and account owner.
- For risk operations: add device, IP, velocity, chargeback, and dispute fields.
- For product analytics: segment failure rate by app version, platform, checkout step, and payment rail.
- For executive triage: add owner, severity, root cause, next action, and expected GMV recovery.

Keep the repo focused on transaction diagnostics. Monthly portfolio health and executive KPI reporting belong in the payments business management repo.

## Portfolio Note

This repo is the supporting technical fintech analytics asset in my Founder's Office / startup operator portfolio. It demonstrates transaction-level SQL diagnostics, failed-GMV analysis, payment reliability monitoring, merchant/bank variance, and risk-signal investigation. It complements, rather than duplicates, the payments business management command center.
