"""
Day 13 Activity: Large Dataset Cleaning
Tasks:
1) Read CSV in chunks
2) Clean each chunk (e.g., numeric conversion)
3) Append cleaned chunks to output CSV
4) Track basic performance metrics
"""

import pandas as pd
import time

# TODO: Implement clean_chunk(df)
# TODO: Implement process_large_file(path_in, path_out, chunksize)

total_rows, sum_income = 0, 0.0
for chunk in pd.read_csv("day13_large_users.csv", chunksize=1000): 
    total_rows += len(chunk)
    sum_income += chunk["income"].sum()
mean_income = sum_income / total_rows
print(f"Mean income: {mean_income:.2f}")