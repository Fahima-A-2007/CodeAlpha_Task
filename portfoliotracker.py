stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "MSFT": 300,
    "GOOG": 2800,
    "AMZN": 3300
}

total_investment = 0

while True:
    stock = input("Enter stock symbol (or 'done' to finish): ").upper()
    if stock == "DONE":
        break

    if stock not in stock_prices:
        print("Stock not found!")
        continue

    quantity = int(input(f"Enter quantity of {stock}: "))
    total_investment += stock_prices[stock] * quantity

print("\nTotal Investment Value: $", total_investment)
