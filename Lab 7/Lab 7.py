import pandas as pd
import numpy as np

data = {
    'customer_id': [1,2,3,4,5,6,7,8,9,10],
    'age': [25,25,np.nan,45,28,np.nan,25,40,29,35],
    'purchase_amount': [5000,5000,4800,np.nan,5300,5000,np.nan,7100,5000,6800],
    'product': ['Laptop','Laptop','Phone','Tablet','Laptop','Tablet','Phone','Laptop','Phone',np.nan],
    'city': ['Riyadh','Jeddah','Riyadh','Jeddah','Riyadh','Riyadh','Jeddah','Riyadh','Jeddah','Riyadh']
}

df = pd.DataFrame(data)
print(df)
print(df.isnull().sum())
print(df['product'].value_counts())
print(df['age'].value_counts())
print(df['purchase_amount'].value_counts())
mean_age = df['age'].mean()
median_amount = df['purchase_amount'].median()
mode_product = df['product'].mode()[0]
df['age_mean'] = df['age'].fillna(mean_age)
df['amount_median'] = df['purchase_amount'].fillna(median_amount)
df['product_mode'] = df['product'].fillna(mode_product)
df['age_ffill'] = df['age'].ffill()
df['age_bfill'] = df['age'].bfill()
print(df)