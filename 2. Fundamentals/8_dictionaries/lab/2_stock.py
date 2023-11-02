products = input().split()

dict_product = dict()

for item in range(0, len(products), 2):
    stock, quantity = products[item], int(products[item + 1])

    dict_product[stock] = quantity

search_items = input().split()

for product in search_items:

    if product in dict_product:
        print(f"We have {dict_product[product]} of {product} left.")

    else:
        print(f"Sorry, we don't have {product}")
