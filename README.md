# SaaS Revenue & Churn Analytics Dashboard

A Revenue Intelligence System That Exposes Hidden Churn and False Growth in SaaS Businesses

## Live Dashboard

[View Live Dashboard](https://saas-churn-dashboard-khmwoycjwsrhnsrdonappa2.streamlit.app/)

## Project Overview

Most SaaS businesses track total MRR and assume growth equals health.MRR is a net number,
It hides churn. Few track where that MRR is actually 
coming from and more importantly, where it is quietly leaking out.

This project builds a complete revenue intelligence system across five analytical 
layers, answering the questions a SaaS CFO or Head of Revenue actually needs answered:

-Is this business growing or just replacing lost customers fast enough to look like it is?
- Which customer cohorts retain best — and when do they start leaving?
- What is each customer tier actually worth over their lifetime?
- Under what conditions does Net Revenue Retention fall below 100%?
- How does a stress period affect cash generation across the customer base?

## Key Findings

| Metric | Value |
|---|---|
| MRR Growth (24 months) | 92.6% ($64K → $123K) |
| Normal Period Churn | 4.9% monthly |
| Stress Period Churn | 11.6% monthly (2.4x normal) |
| Enterprise LTV | $19,960 |
| Starter LTV | $512 |
| LTV Difference | 39x between tiers |
| Healthy NRR Months | 2 out of 23 |
| 12-Month Cohort Retention | 49.2% |

## The Core Insight

A SaaS business growing at 92% over 24 months sounds healthy.

But when churn spikes 2.4x during a stress period, NRR drops below 100% for 
19 consecutive months — meaning the existing customer base is shrinking in value 
faster than expansion revenue can compensate.

The business is not growing. It is replacing lost revenue with new revenue 
at an increasing cost. That is an unsustainable trajectory without direct 
intervention on retention.

## Tech Stack

| Layer | Tool |
|---|---|
| Data Simulation | Python (Pandas, NumPy, Faker) |
| Data Storage | Google BigQuery |
| SQL Analytics | BigQuery Python Client |
| Visualization | Plotly, Matplotlib, Seaborn |
| Dashboard | Streamlit |
| Deployment | Streamlit Cloud |
| Version Control | GitHub |

## Project Architecture
```
saas-churn-dashboard/
├── data/
│   ├── mrr_waterfall.csv       # Monthly MRR breakdown by movement type
│   ├── churn_trend.csv         # Monthly churn rate with period flags
│   ├── cohort_retention.csv    # Cohort retention rates across 12 months
│   ├── ltv_analysis.csv        # Lifetime value by pricing tier
│   └── nrr.csv                 # Net Revenue Retention by month
├── app.py                      # Streamlit dashboard application
└── requirements.txt            # Python dependencies
```

## Dataset

This project uses synthetic data simulating a SaaS business with three 
pricing tiers across 24 months, The dataset was engineered to simulate failure, not just growth.

The simulation includes:

- **1,449 customers** across Starter ($49), Growth ($149), and Enterprise ($499) tiers
- **Realistic seasonality** in monthly signup patterns
- **Tier-differentiated churn** — Enterprise churns at 2%, Starter at 9.6%
- **Expansion revenue** from tier upgrades
- **Deliberate stress period** (Feb–Jun 2024) with 2.2x churn multiplier

## Dashboard Features

- **KPI Cards** — Total MRR, Stress Period Churn, Enterprise LTV, NRR Health
- **MRR Waterfall** — New, Expansion, Retained, and Churned MRR by month
- **Churn Rate Chart** — Monthly churn colored by period with normal average line
- **NRR Trend** — Net Revenue Retention with 100% and 90% threshold lines
- **Cohort Heatmap** — Retention rates across 12 cohorts and 12 months
- **LTV by Tier** — Lifetime value comparison across pricing tiers
- **Interactive Filters** — Filter by period and tier across all charts

## Methodology Note

BigQuery was used as the cloud data warehouse — five structured tables were 
uploaded and analytical queries were executed via the BigQuery Python client. 
The primary analytical and visualization layer was built in Python using 
Pandas, Plotly, Matplotlib, and Seaborn.

## About

Built by **Tobou Egbekun** — Analytics Engineer & Financial Modeler  
Lagos, Nigeria | [LinkedIn](https://linkedin.com/in/tobouegbekun)
