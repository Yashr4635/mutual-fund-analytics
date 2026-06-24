import pandas as pd
from pathlib import Path

Path("data/processed").mkdir(parents=True, exist_ok=True)

# =========================
# NAV HISTORY
# =========================

nav = pd.read_csv("data/raw/02_nav_history.csv")

nav["date"] = pd.to_datetime(nav["date"])

nav = nav.sort_values(
    ["amfi_code", "date"]
)

nav = nav.drop_duplicates()

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("✅ NAV cleaned")


# =========================
# INVESTOR TRANSACTIONS
# =========================

txn = pd.read_csv(
    "data/raw/08_investor_transactions.csv"
)

txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.upper()
)

txn["kyc_status"] = (
    txn["kyc_status"]
    .astype(str)
    .str.upper()
)

txn = txn[txn["amount_inr"] > 0]

txn = txn.drop_duplicates()

txn.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("✅ Transactions cleaned")


# =========================
# SCHEME PERFORMANCE
# =========================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "expense_ratio_pct",
    "aum_crore"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

perf = perf.drop_duplicates()

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("✅ Scheme performance cleaned")

print("\n🎉 Day 2 Cleaning Complete")