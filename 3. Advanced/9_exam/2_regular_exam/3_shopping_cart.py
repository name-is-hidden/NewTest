# def shopping_cart(*args):
#     # Product constraints:
#     # Pizza: 4
#     # Soup: 3
#     # Dessert: 2
# 
#     result = {"Pizza": [], "Soup": [], "Dessert": []}
# 
#     for element in args:
#         meal, product = element[0], element[1]
# 
#         if element == "Stop":
#             break
# 
#         if meal == "Pizza":
#             if len(result[meal]) < 4 and product not in result[meal]:
#                 result[meal].append(product)
# 
#         elif meal == "Soup" and product not in result[meal]:
#             if len(result[meal]) < 3:
#                 result[meal].append(product)
# 
#         elif meal == "Dessert" and product not in result[meal]:
#             if len(result[meal]) < 2:
#                 result[meal].append(product)
# 
#     sorted_result = sorted([f"{key}: {value}" for key, value in sorted(result.items(), key=lambda x: x[0])])
# 
#     if not result.values():
#         return "No products in the cart!"
# 
#     else:
#         return "\n".join(sorted_result)
# 
# 
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Soup', 'carrots'),
#     ('Pizza', 'cheese'),
#     ('Pizza', 'flour'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'mushrooms'),
#     ('Pizza', 'tomatoes'),
#     'Stop',
# ))
# 
# print("-------------------------------")
# 
# print(shopping_cart(
#     ('Pizza', 'ham'),
#     ('Dessert', 'milk'),
#     ('Pizza', 'ham'),
#     'Stop',
# ))
# 
# print("-------------------------------")
# 
# print(shopping_cart(
#     'Stop',
#     ('Pizza', 'ham'),
#     ('Pizza', 'mushrooms'),
# ))

def shopping_cart(*args):
    product_limitations = {"Soup": 3, "Pizza": 4, "Dessert": 2}
    products_dictionary = {"Soup": [], "Pizza": [], "Dessert": []}

    for product in args:
        if product == "Stop":
            break

        if product[1] in products_dictionary[product[0]]:
            continue

        if len(products_dictionary[product[0]]) == product_limitations[product[0]]:
            continue

        products_dictionary[product[0]].append(product[1])

    result = ''

    sorted_dict = {k: v for k, v in (sorted(products_dictionary.items(), key=lambda x: (-len(x[1]), x[0])))}

    for k, v in sorted_dict.items():
        result += f"{k}:\n"

        for val in sorted(v):
            result += f" - {val}\n"

    return result if any(products_dictionary.values()) else "No products in the cart!"
