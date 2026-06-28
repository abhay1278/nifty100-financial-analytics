import sqlite3

conn = sqlite3.connect("data/db/nifty100.db")

cursor = conn.cursor()

cursor.execute("PRAGMA foreign_key_check")

rows = cursor.fetchall()

if len(rows) == 0:
    print("Foreign Key Check : PASS")
else:
    print("Foreign Key Violations Found")
    print(rows)

conn.close()