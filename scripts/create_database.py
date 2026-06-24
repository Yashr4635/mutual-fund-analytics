import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///bluestock_mf.db")

fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav = pd.read_csv("data/processed/02_nav_history_clean.csv")
performance = pd.read_csv("data/processed/07_scheme_performance_clean.csv")
transactions = pd.read_csv("data/processed/08_investor_transactions_clean.csv")

fund_master.to_sql(
    "fund_master",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "nav_history",
    engine,
    if_exists="replace",
    index=False
)

performance.to_sql(
    "scheme_performance",
    engine,
    if_exists="replace",
    index=False
)

transactions.to_sql(
    "investor_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("Database Created Successfully")