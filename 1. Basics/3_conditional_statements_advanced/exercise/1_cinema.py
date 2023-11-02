projection_type = input()
rows = int(input())
columns = int(input())

price = 0
income = 0

if projection_type == "Premiere":
    price = 12.00
    income = price * rows * columns
    print(f"{income:.2f}")

elif projection_type == "Normal":
    price = 7.50
    income = price * rows * columns
    print(f"{income:.2f}")

elif projection_type == "Discount":
    price = 5.00
    income = price * rows * columns
    print(f"{income:.2f}")

else:
    pass
