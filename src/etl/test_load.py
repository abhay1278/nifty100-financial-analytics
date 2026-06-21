# test_load.py

from loader import load_excel

df = load_excel("data/raw/companies.xlsx")

print(df.head())
print(df.shape)