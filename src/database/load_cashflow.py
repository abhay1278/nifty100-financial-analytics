import pandas as pd
import sqlite3

cf = pd.read_excel(
    "data/raw/cashflow.xlsx",
    header=1
)

conn = sqlite3.connect(
    "data/db/nifty100.db"
)

cf.to_sql(
    "cashflow",
    conn,
    if_exists="append",
    index=False
)

print(
    f"{len(cf)} cash flow records loaded"
)

conn.close()