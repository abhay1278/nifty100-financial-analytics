import sqlite3
import pandas as pd

conn = sqlite3.connect("data/db/nifty100.db")

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow",
    "analysis",
    "documents",
    "prosandcons",
    "sectors",
    "stock_prices",
    "market_cap",
    "financial_ratios",
    "peer_groups"
]

results = []

cursor = conn.cursor()

for table in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    count = cursor.fetchone()[0]

    results.append({
        "table_name": table,
        "rows_loaded": count,
        "status": "SUCCESS"
    })

audit = pd.DataFrame(results)

audit.to_csv(
    "output/load_audit.csv",
    index=False
)

print(audit)

conn.close()

print("\nload_audit.csv generated successfully.")