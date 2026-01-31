def remove_currency(value):
    return float(value.replace('$', '').replace(',', ''))

def calculate_product_total(price, qty):
    return price * qty

def classify_price(amount):
    if amount < 1000:
        return "low"
    elif amount < 2000:
        return "med"
    else:
        return "high"