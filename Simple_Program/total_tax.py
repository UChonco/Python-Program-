def total_cost(prices,tax_rate):
    subtotal =sum(prices)
    tax = subtotal * tax_rate
    total_cost = subtotal  + tax
    return total_cost


item_prices = [12.99, 23.50, 9.99, 5.49]  # Example prices of items
tax_rate = 0.07  # Example tax rate of 7%

total = total_cost(item_prices, tax_rate)
print(f"Total cost including tax: ${total:.2f}")
