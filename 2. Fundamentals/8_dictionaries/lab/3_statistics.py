text = input()

dict_products = dict()

while text != "statistics":
    data = text.split(": ")

    product, quantity = data[0], int(data[1])

    if product not in dict_products:
        dict_products[product] = 0

    dict_products[product] += quantity

    text = input()

print("Products in stock:")

for product, quantity in dict_products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(dict_products)}")
print(f"Total Quantity: {sum(dict_products.values())}")
