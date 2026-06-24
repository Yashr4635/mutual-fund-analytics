# Data Dictionary

## fund_master

| Column | Description |
|----------|----------|
| amfi_code | Unique fund identifier |
| fund_house | Mutual fund company |
| scheme_name | Scheme name |
| category | Fund category |
| sub_category | Fund sub-category |
| plan | Regular or Direct plan |
| launch_date | Fund launch date |
| benchmark | Benchmark index |
| expense_ratio_pct | Expense ratio percentage |
| fund_manager | Fund manager name |
| risk_category | Risk level |

---

## nav_history

| Column | Description |
|----------|----------|
| amfi_code | Fund identifier |
| date | NAV date |
| nav | Net Asset Value |

---

## scheme_performance

| Column | Description |
|----------|----------|
| amfi_code | Fund identifier |
| scheme_name | Scheme name |
| return_1yr_pct | 1 year return |
| return_3yr_pct | 3 year return |
| return_5yr_pct | 5 year return |
| alpha | Alpha value |
| beta | Beta value |
| sharpe_ratio | Risk-adjusted return |
| aum_crore | Assets under management |
| expense_ratio_pct | Expense ratio percentage |
| risk_grade | Risk grade |

---

## investor_transactions

| Column | Description |
|----------|----------|
| investor_id | Unique investor ID |
| transaction_date | Date of transaction |
| amfi_code | Fund identifier |
| transaction_type | SIP, Lumpsum, Redemption |
| amount_inr | Transaction amount |
| state | Investor state |
| city | Investor city |
| city_tier | Tier of city |
| age_group | Investor age group |
| gender | Investor gender |
| annual_income_lakh | Annual income |
| payment_mode | Payment method |
| kyc_status | KYC verification status |