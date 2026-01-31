import pandas as pd
from functions import remove_currency, calculate_product_total, classify_price
raw = {
    "product": ["Widget A", "Widget B", "Widget C"],
    "price": ["$1,234.50", "$567.89", "$2,345.00"],
    "quantity": [10, 5, None],
}
df = pd.DataFrame(raw)
df['price'] = df['price'].apply(remove_currency)
df['quantity'] = df['quantity'].fillna(0)
df['total'] = df.apply(lambda row: calculate_product_total(row['price'], row['quantity']), axis=1)
df['price_category'] = df['price'].apply(classify_price)
print(df)