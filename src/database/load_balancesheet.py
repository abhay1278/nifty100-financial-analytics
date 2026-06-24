import pandas as pd
import sqlite3

bs = pd.read_excel(
    "data/raw/balancesheet.xlsx",
    header=1
)

conn = sqlite3.connect(
    "data/db/nifty100.db"
)

bs.to_sql(
    "balancesheet",
    conn,
    if_exists="append",
    index=False
)

print(
    f"{len(bs)} balance sheet records loaded"
)

conn.close()