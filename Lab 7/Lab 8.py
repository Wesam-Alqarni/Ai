import numpy as np
import pandas as pd
def detect_outliers_iqr(df):
    Q1 = df.quantile(0.25)
    Q3 = df.quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    return ((df < lower) | (df > upper))
def remove_outliers_iqr(df):
    outliers = detect_outliers_iqr(df)
    return df[~outliers.any(axis=1)]
def normalize_data(df):
    return (df - df.min()) / (df.max() - df.min())
def standardize_data(df):
    return (df - df.mean()) / df.std()
data_with_outliers = pd.DataFrame({
    'House_Price': [250000, 275000, 300000, 325000, 350000, 375000, 400000, 1500000],
    'Square_Feet': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 5000],
    'Bedrooms': [3, 3, 4, 4, 5, 5, 6, 10]
})
different_values_data = pd.DataFrame({
    'Temperature': [22.5, 23.1, 24.3, 25.7, 26.2, 27.8, 28.4, 29.9, 30.5, 31.2],
    'Humidity': [45, 47, 49, 52, 55, 58, 62, 65, 68, 70],
    'Pressure': [1013, 1012, 1011, 1010, 1009, 1008, 1007, 1006, 1005, 1004]
})
outliers1 = detect_outliers_iqr(data_with_outliers)
cleaned1 = remove_outliers_iqr(data_with_outliers)
norm1 = normalize_data(cleaned1)
std1 = standardize_data(cleaned1)
outliers2 = detect_outliers_iqr(different_values_data)
cleaned2 = remove_outliers_iqr(different_values_data)
norm2 = normalize_data(cleaned2)
std2 = standardize_data(cleaned2)           
print("Dataset 1 - Outliers detected:")
print(outliers1)
print("\nDataset 1 - Normalized:")
print(norm1)
print("\nDataset 1 - Standardized:")
print(std1)
print("\nDataset 2 - Outliers detected:")
print(outliers2)
print("\nDataset 2 - Normalized:")
print(norm2)
print("\nDataset 2 - Standardized:")
print(std2)