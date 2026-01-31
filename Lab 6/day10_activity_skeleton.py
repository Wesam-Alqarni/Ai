"""
Day 10 Activity: Outliers Practice
Tasks:
1) Implement IQR-based outlier detection
2) Implement z-score detection
3) Compare strategies: no handling, IQR capping, log1p transform
"""

import numpy as np
import pandas as pd

# Sample heavy-tailed data
np.random.seed(10)
values = np.concatenate([np.random.lognormal(10, 0.5, 1000), [1e7, 2e7]])

df = pd.DataFrame({"income": values})

def iqr_bounds(data, col):
    q1 = data[col].quantile(0.25)
    q3 = data[col].quantile(0.75)
    iqr = q3 - q1
    lower = q1 - 1.5*iqr
    upper = q3 + 1.5*iqr
    return lower, upper
def detect_outliers_iqr(data, col):
    lower, upper = iqr_bounds(data, col)
    outliers = data[(data[col] < lower) | (data[col] > upper)]
    return outliers
def detect_outliers_zscore(data, col):
    z_scores = np.abs(stats.zscore(data[col]))
    outliers = data[z_scores > 3]
    return outliers
iqr_outliers = detect_outliers_iqr(df, "income")
zscore_outliers = detect_outliers_zscore(df, "income")
lower, upper = iqr_bounds(df, "income")
df_capped = df.copy()
df_capped["income"] = np.clip(df_capped["income"], lower, upper)
df_log = df.copy()
df_log["income"] = np.log1p(df_log["income"])
