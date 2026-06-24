import pandas as pd
from sqlalchemy import create_engine

print("Creating SQLite Database...")

engine = create_engine("sqlite:///bluestock_mf.db")

# Load datasets
fund_master = pd.read_csv(
    "data/raw/01_fund_master.csv"
)

nav_history = pd.read_csv(
    "data/processed/02_nav_history_clean.csv"
)

scheme_performance = pd.read_csv(
    "data/processed/07_scheme_performance_clean.csv"
)

investor_transactions = pd.read_csv(
    "data/processed/08_investor_transactions_clean.csv"
)

# Load into SQLite
fund_master.to_sql(
    "fund_master",
    engine,
    if_exists="replace",
    index=False
)

nav_history.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

scheme_performance.to_sql(
    "scheme_performance",
    engine,
    if_exists="replace",
    index=False
)

investor_transactions.to_sql(
    "investor_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("✅ Database Created Successfully")