import pandas as pd
import sqlite3

conn = sqlite3.connect("data/db/nifty100.db")

tables = [
    ("documents.xlsx", "documents", 1),
    ("prosandcons.xlsx", "prosandcons", 1),
    ("sectors.xlsx", "sectors", 0),
    ("stock_prices.xlsx", "stock_prices", 0),
    ("market_cap.xlsx", "market_cap", 0),
    ("financial_ratios.xlsx", "financial_ratios", 0),
    ("peer_groups.xlsx", "peer_groups", 0)
]

for file, table, header in tables:

    df = pd.read_excel(
        f"data/raw/{file}",
        header=header
    )

    df.to_sql(
        table,
        conn,
        if_exists="append",
        index=False
    )

    print(f"{table}: {len(df)} rows loaded")

conn.close()

print("\nAll remaining tables loaded successfully.")