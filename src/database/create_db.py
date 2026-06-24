import sqlite3

conn = sqlite3.connect(
    "data/db/nifty100.db"
)

cursor = conn.cursor()

with open("db/schema.sql","r") as f:
    cursor.executescript(
        f.read()
    )

conn.commit()

print("Database created successfully")

conn.close()