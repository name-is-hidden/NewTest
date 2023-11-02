products = input().split()

bakery_dict = dict()

for item in range(0, len(products), 2):
    stock, price = products[item], int(products[item + 1])

    if stock not in bakery_dict:
        bakery_dict[stock] = price

print(bakery_dict)