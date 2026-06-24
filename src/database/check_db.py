import sqlite3

conn = sqlite3.connect(
    "data/db/nifty100.db"
)

cursor = conn.cursor()

cursor.execute(
    "SELECT COUNT(*) FROM companies"
)

print(
    cursor.fetchone()
)

conn.close()