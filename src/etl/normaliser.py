# src/etl/normaliser.py

import pandas as pd

def normalize_ticker(ticker):
    if pd.isna(ticker):
        return None

    return str(ticker).strip().upper()


def normalize_year(year):
    if pd.isna(year):
        return None

    try:
        return pd.to_datetime(year).strftime("%Y-%m")
    except:
        return str(year)
    
if __name__ == "__main__":
    print(normalize_ticker(" tcs "))
    print(normalize_year("2024"))

import pandas as pd

def normalize_ticker(ticker):
    if pd.isna(ticker):
        return None
    return str(ticker).strip().upper()

def normalize_year(year):
    if pd.isna(year):
        return None

    try:
        return pd.to_datetime(year).strftime("%Y-%m")
    except:
        return str(year)