# Fintech Transaction Monitoring System

**End-to-end payments analytics pipeline** monitoring 50,000+ transactions 
across GMV tracking, failure diagnosis, risk scoring, and merchant analytics.

Built to replicate how fintech companies like Slice, Razorpay, and Paytm 
monitor payment health and diagnose revenue leakage in real time.

---

## Key Metrics

| Metric | Value |
|---|---|
| Transactions Analyzed | 50,000+ |
| KPIs Tracked | GMV, Failed GMV, Success Rate, Transaction Volume |
| Risk Signals | High-frequency users, repeated failures, high-value anomalies |
| SQL Query Modules | 5 (EDA → KPI → Risk → Advanced → Business Questions) |

---

## The Problem

Payment systems process thousands of transactions per minute. Even small 
failure rates cause revenue leakage, poor UX, and operational blind spots.

**Key questions this system answers:**
- What are the main drivers of failed transactions?
- When do failures spike — and why?
- Which merchants contribute most to revenue loss?
- Which banks and payment methods are least reliable?
- Which users show high-risk behavior and need investigation?

---

## Key Findings

- **UNKNOWN errors** are the primary failure driver — a system-level issue, not user behavior
- **Failures spike post 7 PM** — peak-load stress, not fraud
- **Top merchants (Pareto effect)** — a small set drives a disproportionate share of failed GMV
- **Bank-level variance** — certain banks show consistently higher failure rates
- **High-risk users** exhibit repeated high-value transactions with failure patterns

---

## Design Decisions

**Rule-based risk detection over ML** — chosen for interpretability and faster 
iteration. In early-stage fintech systems, ops teams need to explain flags to 
compliance. Black-box models create friction.

**KPI-first monitoring** — GMV, Success Rate, and Failed GMV directly track 
business impact before diving into complex models.

**Batch analytics over real-time** — implemented for simplicity and portability. 
Real-time streaming (Kafka) is the natural next step for production deployment.

**Top-N views for clarity** — Pareto-style merchant and user ranking keeps 
dashboards actionable and avoids information overload.

---

## Dashboard Preview

![Fintech Transaction Dashboard](dashboard/screenshots/fintech_dashboard_preview.png)

**[Open Live Tableau Dashboard](https://public.tableau.com/views/PaymentsTransactionsAnalyticsMonitoring/Dashboard1)**  
No setup required — explore filters, drill-downs, and risk patterns directly.

---

## Tech Stack

`Python` · `SQL` · `Pandas` · `Tableau Public`

**Pipeline:**

Raw Data → Python Processing → SQL Analysis → Tableau Dashboard

---

## How to Run

```bash
# 1. Clone the repo and install dependencies
pip install -r requirements.txt

# 2. Generate synthetic dataset
python src/generate_dataset.py

# 3. Validate dataset
python src/dataset_validation.py

# 4. Run SQL queries in your client against the processed data
# 5. Open dashboard/tableau_dashboard.twbx in Tableau
```

---

## Real-World Application

Mirrors monitoring infrastructure used by fintech ops and product teams to:
- Reduce failed GMV by identifying top failure drivers early
- Improve system reliability via peak-load monitoring
- Enable proactive fraud detection using behavioral signals
- Give product and ops teams actionable, self-serve dashboards

---

*Part of a portfolio targeting analyst roles at Series A+ startups.*  
*[← Back to Profile](https://github.com/shubham1502-hue)*
