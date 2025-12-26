# Business Data Analytics: Profitability Script
products = [
    {"name": "Laptop", "revenue": 1200, "cost": 800},
    {"name": "Mouse", "revenue": 50, "cost": 10},
    {"name": "Monitor", "revenue": 300, "cost": 150}
]

print("--- Product Profitability Report ---")
for p in products:
    profit = p["revenue"] - p["cost"]
    margin = (profit / p["revenue"]) * 100
    print(f"Product: {p['name']} | Profit: ${profit} | Margin: {margin:.2f}%")
