import pandas as pd
import sqlite3

# Read companies file
companies = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

# Keep only schema columns
companies = companies[
    [
        "id",
        "company_name",
        "website",
        "face_value",
        "book_value",
        "roce_percentage",
        "roe_percentage"
    ]
]

# Connect database
conn = sqlite3.connect(
    "data/db/nifty100.db"
)

# Load data
companies.to_sql(
    "companies",
    conn,
    if_exists="append",
    index=False
)

print(
    f"{len(companies)} companies loaded successfully"
)

conn.close()