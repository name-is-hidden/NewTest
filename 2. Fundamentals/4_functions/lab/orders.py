def total_price(product, quantity):

    if product == "coffee":
        return quantity * 1.5           # price for a single coffee is 1.50

    elif product == "water":
        return quantity * 1            # price for a single bottle of water is 1.00

    elif product == "coke":
        return quantity * 1.4           # price for a single coke is 1.40

    elif product == "snacks":
        return quantity * 2            # price for single snack is 2.00


stock = input()
stock_quantity = int(input())

stock_price = total_price(stock, stock_quantity)

print(f"{stock_price:.2f}")
