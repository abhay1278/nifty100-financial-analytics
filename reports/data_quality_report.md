# Data Quality Report

## Foreign Key Validation

Status: WARNING

Observation:

Foreign key validation identified records in Profit & Loss, Balance Sheet,
Cash Flow, Financial Ratios, Analysis and Documents whose company_id values
are not present in the Companies master table.

Root Cause:

The source datasets are inconsistent. Some financial datasets contain
companies that are missing from the master company dataset.

Impact:

These records cannot satisfy referential integrity constraints.

Recommendation:

Update the Companies master dataset to include the missing company IDs
or exclude orphan records during ETL processing.