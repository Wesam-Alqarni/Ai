"""
Day 7 Activity: Imputation Practice
Tasks:
1) Implement fit_imputer(train_df) returning medians/modes
2) Implement transform_imputer(df, params)
3) Add missing indicators optionally
4) Compare behavior with/without indicators
"""

import pandas as pd
# Sample dataset
train = pd.DataFrame({
    "age": [25, None, 40, 33],
    "city": ["NY", "SF", None, "NY"],
})
test = pd.DataFrame({
    "age": [None, 50],
    "city": ["SF", None],
})
def fit_imputer(train_df):
    params = {}
    params["age"] = train_df["age"].median()
    params["city"] = train_df["city"].mode()[0]
    return params
def transform_imputer(df, params, add_indicators=True):
    df_copy = df.copy()
    if add_indicators:
        df_copy["age_missing"] = df_copy["age"].isnull().astype(int)
        df_copy["city_missing"] = df_copy["city"].isnull().astype(int)
    df_copy["age"] = df_copy["age"].fillna(params["age"])
    df_copy["city"] = df_copy["city"].fillna(params["city"])
    return df_copy
params = fit_imputer(train)
train_imputed = transform_imputer(train, params, add_indicators=True)
test_imputed = transform_imputer(test, params, add_indicators=True)
print(train_imputed)
print(test_imputed)