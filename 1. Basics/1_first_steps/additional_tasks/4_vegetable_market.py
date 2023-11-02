# Write a program that calculates the profit from vegetables and fruit sales:

vegetables = float(input())
fruit = float(input())
vegetables_amount = int(input())
fruit_amount = int(input())

euro_conversion = 1.94

vegetables_price = vegetables * vegetables_amount

fruit_price = fruit * fruit_amount

total_price = (vegetables_price + fruit_price) / euro_conversion

print(f"{total_price:.2f}")
