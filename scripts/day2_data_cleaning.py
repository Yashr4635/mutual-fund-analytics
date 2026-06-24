import pandas as pd
from pathlib import Path

# Create processed folder if it doesn't exist
Path("data/processed").mkdir(parents=True, exist_ok=True)

print("Starting Day 2 Data Cleaning...")

# =====================================
# 1. CLEAN NAV HISTORY
# =====================================

nav = pd.read_csv("data/raw/02_nav_history.csv")

# Convert date column
nav["date"] = pd.to_datetime(nav["date"])

# Sort data
nav = nav.sort_values(["amfi_code", "date"])

# Remove duplicates
nav = nav.drop_duplicates()

# Fill missing NAV values
nav["nav"] = nav.groupby("amfi_code")["nav"].ffill()

# Keep only valid NAV values
nav = nav[nav["nav"] > 0]

nav.to_csv(
    "data/processed/02_nav_history_clean.csv",
    index=False
)

print("✅ NAV History cleaned")

# =====================================
# 2. CLEAN INVESTOR TRANSACTIONS
# =====================================

txn = pd.read_csv("data/raw/08_investor_transactions.csv")

# Standardize transaction type
txn["transaction_type"] = (
    txn["transaction_type"]
    .astype(str)
    .str.upper()
)

# Standardize KYC status
txn["kyc_status"] = (
    txn["kyc_status"]
    .astype(str)
    .str.upper()
)

# Convert transaction date
txn["transaction_date"] = pd.to_datetime(
    txn["transaction_date"]
)

# Keep valid amounts
txn = txn[txn["amount_inr"] > 0]

# Remove duplicates
txn = txn.drop_duplicates()

txn.to_csv(
    "data/processed/08_investor_transactions_clean.csv",
    index=False
)

print("✅ Investor Transactions cleaned")

# =====================================
# 3. CLEAN SCHEME PERFORMANCE
# =====================================

perf = pd.read_csv(
    "data/raw/07_scheme_performance.csv"
)

numeric_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in numeric_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Expense ratio validation
perf = perf[
    (perf["expense_ratio_pct"] >= 0.1)
    &
    (perf["expense_ratio_pct"] <= 2.5)
]

# Remove duplicates
perf = perf.drop_duplicates()

perf.to_csv(
    "data/processed/07_scheme_performance_clean.csv",
    index=False
)

print("✅ Scheme Performance cleaned")

print("\n🎉 Day 2 Cleaning Complete")