import pandas as pd
import sqlite3

analysis = pd.read_excel(
    "data/raw/analysis.xlsx",
    header=1
)

conn = sqlite3.connect(
    "data/db/nifty100.db"
)

analysis.to_sql(
    "analysis",
    conn,
    if_exists="append",
    index=False
)

print(f"{len(analysis)} analysis records loaded")

conn.close()