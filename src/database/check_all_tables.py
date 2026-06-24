import sqlite3

conn = sqlite3.connect(
    "data/db/nifty100.db"
)

cursor = conn.cursor()

tables = [
    "companies",
    "profitandloss",
    "balancesheet",
    "cashflow"
]

for table in tables:

    cursor.execute(
        f"SELECT COUNT(*) FROM {table}"
    )

    count = cursor.fetchone()[0]

    print(
        f"{table}: {count}"
    )

conn.close()