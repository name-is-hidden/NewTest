text = input()

products_dict = dict()

while text != 'buy':
    line = text.split()

    product, price, quantity = line[0], float(line[1]), int(line[2])

    if product not in products_dict:
        products_dict[product] = [price, quantity]

    else:
        products_dict[product] = [price, (quantity + products_dict[product][1])]

    text = input()

for key, value in products_dict.items():
    print(f'{key} -> {(value[0] * value[1]):.2f}')
