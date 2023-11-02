import re


expression = r">>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)"
final_price = 0
furniture = list()

while True:
    text = input()

    if text == "Purchase":
        break

    matches = re.match(expression, text)

    if matches is not None:
        product, price, quantity = matches[1], float(matches[2]), int(matches[3])
        final_price += price * quantity
        furniture.append(product)

print("Bought furniture:")

if final_price > 0:
    print("\n".join(furniture))

print(f"Total money spend: {final_price:.2f}")
