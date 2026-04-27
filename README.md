# 🏦 Bank Customer Churn Analysis

**Tools:** Python · Pandas · Matplotlib · Seaborn  
**Dataset:** [Churn Modelling Dataset — Kaggle](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)  
**Author:** Ranim

---

## 📌 Project Overview

Customer churn is one of the most costly problems a bank can face — losing an existing customer is far more expensive than acquiring a new one. This project analyses **10,000 bank customers** to identify the key factors that drive churn and uncover which customer segments are most at risk.

This is the kind of analysis a Data Analyst would deliver to a retention or marketing team.

---

## ❓ Business Questions Answered

1. What is the overall churn rate?
2. Which countries have the highest churn?
3. Do men or women churn more?
4. Which age groups are most at risk?
5. Does the number of products affect churn?
6. How does account balance differ between churned and retained customers?
7. Are inactive members more likely to leave?

---

## 📊 Charts Generated

| File | Description |
|---|---|
| `01_churn_rate.png` | Overall churn vs retained breakdown |
| `02_churn_by_geography.png` | Churn rate by country (France, Germany, Spain) |
| `03_churn_by_gender.png` | Churn rate by gender |
| `04_churn_by_age.png` | Churn rate across age groups |
| `05_churn_by_products.png` | Churn rate by number of products held |
| `06_balance_distribution.png` | Account balance: churned vs retained |
| `07_churn_by_active_member.png` | Active vs inactive member churn comparison |

---

## 🔍 Key Insights

- 📌 **Overall churn rate is ~20%** — 2,037 out of 10,000 customers left
- 🇩🇪 **Germany has the highest churn** at ~32%, nearly double France and Spain
- 👩 **Female customers churn more** than male customers (~25% vs ~16%)
- 📅 **Customers aged 41–50 are most at risk**, with churn rates peaking in this group
- 🏦 **Customers with 3–4 products churn at nearly 100%** — a critical red flag
- 💰 **Churned customers tend to hold higher balances** — the bank is losing valuable clients
- 💤 **Inactive members churn at almost 2× the rate** of active members

---

## 🗂️ Files in This Repository

```
bank-churn-analysis/
│
├── README.md                    ← You are here
├── bank_churn_analysis.py       ← Full Python analysis script
├── 01_churn_rate.png            ← Generated chart
├── 02_churn_by_geography.png    ← Generated chart
├── 03_churn_by_gender.png       ← Generated chart
├── 04_churn_by_age.png          ← Generated chart
├── 05_churn_by_products.png     ← Generated chart
├── 06_balance_distribution.png  ← Generated chart
└── 07_churn_by_active_member.png← Generated chart
```

---

## ▶️ How to Run

**1. Install required libraries:**
```bash
pip install pandas matplotlib seaborn
```

**2. Download the dataset:**
- Go to [Kaggle — Churn Modelling Dataset](https://www.kaggle.com/datasets/shrutimechlearn/churn-modelling)
- Download `Churn_Modelling.csv`
- Place it in the same folder as the script

**3. Run the script:**
```bash
python bank_churn_analysis.py
```

All 7 charts will be saved automatically to the same folder.

---

## 🛠️ Libraries Used

| Library | Purpose |
|---|---|
| `pandas` | Data loading, cleaning, and aggregation |
| `matplotlib` | Chart creation and customisation |
| `seaborn` | Visual styling |

---

## 🚀 About This Project

This project is part of my **Data Analyst portfolio**, built during my career transition into tech. It demonstrates:

- Exploratory Data Analysis (EDA) using Python and Pandas
- Translating data into clear business insights
- Clean, well-commented and readable code
- Data visualisation with Matplotlib and Seaborn

---

## 🔗 Connect With Me

- 💼 [LinkedIn](https://www.linkedin.com/in/ranim-c-07571836a)
- 🐙 [GitHub](https://github.com/Renno2683)
- 📂 [SQL Portfolio](https://github.com/Renno2683/chinook-SQL-portfolio)
- 📊 [Sales Dashboard](https://github.com/Renno2683/Chinook-Sales-Dashboard)
