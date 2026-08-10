def calculate_total(prices):
    total = 0

    for price in prices:
        total += price

    tax = total * 0.18
    discount = 100

    final_amount = total + tax + discount   # <-- BUG HERE
    return final_amount


items = [500, 300, 200]

amount = calculate_total(items)
print("Total:", amount)