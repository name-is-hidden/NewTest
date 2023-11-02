# Calculate the price of the needed products with the given prices:

dog_food_price = 2.50
cat_food_price = 4.00

dog_food_quantity = int(input())
cat_food_quantity = int(input())

total = (dog_food_price * dog_food_quantity) + (cat_food_price * cat_food_quantity)

print(f"{total} lv.")
