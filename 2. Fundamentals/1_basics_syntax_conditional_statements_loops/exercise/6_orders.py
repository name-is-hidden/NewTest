number_of_orders = int(input())

total = 0

for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_count = int(input())

    order_price = price_per_capsule * days * capsules_count
    total += order_price

    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total:.2f}")
