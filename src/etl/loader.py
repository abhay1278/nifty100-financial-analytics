import pandas as pd

files = [
    "companies.xlsx",
    "profitandloss.xlsx",
    "balancesheet.xlsx",
    "cashflow.xlsx",
    "analysis.xlsx",
    "documents.xlsx",
    "prosandcons.xlsx",
    "sectors.xlsx",
    "stock_prices.xlsx",
    "market_cap.xlsx",
    "financial_ratios.xlsx",
    "peer_groups.xlsx"
]

for file in files:

    try:

        if file in [
            "companies.xlsx",
            "profitandloss.xlsx",
            "balancesheet.xlsx",
            "cashflow.xlsx",
            "analysis.xlsx",
            "documents.xlsx",
            "prosandcons.xlsx"
        ]:
            df = pd.read_excel(
                f"data/raw/{file}",
                header=1
            )

        else:
            df = pd.read_excel(
                f"data/raw/{file}",
                header=0
            )

        print(file, df.shape)

    except Exception as e:

        print(file, "ERROR:", e)