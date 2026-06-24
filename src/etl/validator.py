import pandas as pd

validation_results = []

companies = pd.read_excel(
    "data/raw/companies.xlsx",
    header=1
)

print(companies.columns.tolist())
print(companies.head())

profitandloss = pd.read_excel(
    "data/raw/profitandloss.xlsx",
    header=1
)

print("Companies Loaded:", companies.shape)



# DQ-01 Primary Key Uniqueness

duplicates = companies[
    companies["id"].duplicated()
]

if len(duplicates) > 0:

    validation_results.append({
        "rule": "DQ-01",
        "severity": "CRITICAL",
        "count": len(duplicates),
        "message": "Duplicate company IDs"
    })

else:

    validation_results.append({
        "rule": "DQ-01",
        "severity": "PASS",
        "count": 0,
        "message": "No duplicate company IDs"
    })

print(validation_results)

# DQ-02 Company Count Check

if len(companies) == 92:

    validation_results.append({
        "rule": "DQ-02",
        "severity": "PASS",
        "count": 92,
        "message": "Company count matches expected value"
    })

else:

    validation_results.append({
        "rule": "DQ-02",
        "severity": "CRITICAL",
        "count": len(companies),
        "message": "Company count mismatch"
    })



# DQ-03 Missing Company IDs

missing_ids = companies["id"].isna().sum()

validation_results.append({
    "rule": "DQ-03",
    "severity": "WARNING" if missing_ids > 0 else "PASS",
    "count": int(missing_ids),
    "message": "Missing company IDs"
})




# DQ-04 Foreign Key Integrity

company_ids = set(companies["id"])

invalid_fk = profitandloss[
    ~profitandloss["company_id"].isin(company_ids)
]
print(invalid_fk["company_id"].unique())


validation_results.append({
    "rule": "DQ-04",
    "severity": "CRITICAL" if len(invalid_fk) > 0 else "PASS",
    "count": len(invalid_fk),
    "message": "Foreign key integrity check"
})




# DQ-05 Company-Year Duplicate Check

duplicates_year = profitandloss[
    profitandloss.duplicated(
        subset=["company_id", "year"],
        keep=False
    )
]

validation_results.append({
    "rule": "DQ-05",
    "severity": "CRITICAL" if len(duplicates_year) > 0 else "PASS",
    "count": len(duplicates_year),
    "message": "Duplicate company-year records"
})



# DQ-06 Positive Sales Check

negative_sales = profitandloss[
    profitandloss["sales"] <= 0
]

validation_results.append({
    "rule": "DQ-06",
    "severity": "CRITICAL" if len(negative_sales) > 0 else "PASS",
    "count": len(negative_sales),
    "message": "Non-positive sales values"
})

results_df = pd.DataFrame(validation_results)

results_df.to_csv(
    "output/validation_failures.csv",
    index=False
)

print(results_df)

print("\nValidation report saved successfully")