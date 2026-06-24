import pandas as pd
import sqlite3

pnl = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

print(pnl.columns.tolist())
conn = sqlite3.connect(
    "data/db/nifty100.db"
)

pnl.to_sql(
    "profitandloss",
    conn,
    if_exists="append",
    index=False
)

print(
    f"{len(pnl)} profit and loss records loaded"
)

conn.close()