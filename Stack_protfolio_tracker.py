# Predefined stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 170,
    "MSFT": 420,
    "AMZN": 190
}

portfolio = []

total_investment = 0

print("=" * 45)
print("       STOCK PORTFOLIO TRACKER")
print("=" * 45)

print("\nAvailable stocks:")
for stock, price in stock_prices.items():
    print(f"{stock}: ${price}")

print("\nEnter your stock details.")
print("Type 'done' when you have finished.")

while True:

    stock = input("\nEnter stock symbol: ").upper().strip()

    if stock == "DONE":
        break

    # Check whether stock exists
    if stock not in stock_prices:
        print("❌ Stock not available.")
        print("Please choose from:", ", ".join(stock_prices.keys()))
        continue

    # Get quantity
    try:
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("❌ Quantity must be greater than 0.")
            continue

    except ValueError:
        print("❌ Please enter a valid number.")
        continue

    # Calculate investment
    price = stock_prices[stock]
    investment = price * quantity

    total_investment += investment

    # Store information
    portfolio.append({
        "stock": stock,
        "quantity": quantity,
        "price": price,
        "investment": investment
    })

    print(f"✅ {stock} added successfully.")
    print(f"Investment: ${investment}")

# Display portfolio
print("\n" + "=" * 55)
print("              YOUR PORTFOLIO")
print("=" * 55)

if len(portfolio) == 0:
    print("No stocks were added.")

else:
    print(f"{'Stock':<10}{'Quantity':<10}{'Price':<10}{'Investment'}")
    print("-" * 55)

    for item in portfolio:
        print(
            f"{item['stock']:<10}"
            f"{item['quantity']:<10}"
            f"${item['price']:<9}"
            f"${item['investment']}"
        )

    print("-" * 55)
    print(f"Total Investment: ${total_investment}")

    # Save result to text file
    with open("portfolio_result.txt", "w") as file:

        file.write("STOCK PORTFOLIO REPORT\n")
        file.write("=" * 40 + "\n\n")

        for item in portfolio:
            file.write(
                f"Stock: {item['stock']}\n"
                f"Quantity: {item['quantity']}\n"
                f"Price: ${item['price']}\n"
                f"Investment: ${item['investment']}\n\n"
            )

        file.write("=" * 40 + "\n")
        file.write(f"Total Investment: ${total_investment}\n")

    print("\n✅ Result saved to portfolio_result.txt")

print("\nThank you for using Stock Portfolio Tracker!")