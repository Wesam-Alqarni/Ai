"""
Day 6 Activity: Missing Values Practice
Tasks:
1) Load/define a partially observed dataset
2) Normalize missing tokens to NaN
3) Produce missingness summary (per-column %, per-row)
4) Build Version A: drop rows with missing in key cols
5) Build Version B: impute + indicators
6) Compare basic metrics between A and B
"""

import numpy as np
import pandas as pd

# Sample raw dataset (replace or load your own)
raw = {
    "age": [25, "N/A", 40, 33, "?"],
    "income": [50000, 60000, None, "unknown", 80000],
    "churned": [0, 1, 0, 1, 0],
}

df_raw = pd.DataFrame(raw)

df = df_raw.replace(["N/A", "NA", "not reported", "unknown", "?"], np.nan)

def missing_summary(df):
    per_column = df.isnull().mean() * 100
    per_row = df.isnull().sum(axis=1)
    return per_column, per_row

col_missing, row_missing = missing_summary(df)

key_cols = ["age", "income"]
df_a = df.dropna(subset=key_cols)

df_b = df.copy()

for col in ["age", "income"]:
    df_b[f"{col}_missing"] = df_b[col].isnull().astype(int)
    df_b[col] = df_b[col].fillna(df_b[col].mean())

mean_a = df_a[["age", "income"]].mean()
mean_b = df_b[["age", "income"]].mean()

print("Version A means:", mean_a.to_dict())
print("Version B means:", mean_b.to_dict())