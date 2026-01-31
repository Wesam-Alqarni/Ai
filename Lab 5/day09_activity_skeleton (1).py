"""
Day 9 Activity: Data Types Practice
Tasks:
1) Identify numeric-like, currency-like, datetime-like columns
2) Convert to proper dtypes
3) Validate conversions by checking NaN counts
"""

import pandas as pd

raw = {
    "age": ["25", "30", "unknown"],
    "income": ["$50,000", "$60,000", None],
    "signup": ["2024-01-01", "01/05/2024", "not a date"],
}

df = pd.DataFrame(raw)

# TODO: Implement normalize_schema(df) to convert types safely
def normalize_schema(df):
    dfd = df.copy()
    dfd['age'] = pd.to_numeric(dfd['age'], errors='coerce')
    dfd['income'] = dfd['income'].replace({'\$': '', ',': ''}, regex=True)
    dfd['income'] = pd.to_numeric(dfd['income'], errors='coerce')
    dfd['signup'] = pd.to_datetime(dfd['signup'], errors='coerce')
    return dfd
df_normalized = normalize_schema(df)
print(df_normalized.dtypes)
print(df_normalized.isna().sum())
