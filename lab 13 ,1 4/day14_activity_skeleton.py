"""
Day 14 Activity: Full Cleaning Pipeline
Tasks:
1) Build clean_data() that orchestrates type, missing, outliers, strings/dates
2) Add basic validation checks
3) Run end-to-end and inspect
"""

import pandas as pd
import numpy as np

# TODO: Implement clean_types(df)
# TODO: Implement clean_missing(df)
# TODO: Implement handle_outliers(df)
# TODO: Implement clean_strings_and_dates(df)
# TODO: Implement validate_cleaned(df)
# TODO: Implement clean_data(df) that calls the above in order
df = pd.read_csv("day14_users_raw.csv")
def clean_types(df):
    out = df.copy()
    out["age"] = pd.to_numeric(out["age"], errors="coerce")
    out["income"] = pd.to_numeric(out["income"], errors="coerce")
    return out

def clean_missing(df):
    out = df.copy()
    out["age"] = out["age"].fillna(out["age"].median())
    return out
