import math

days_out = int(input())
food = int(input())
dog_food = float(input())
cat_food = float(input())
turtle_food = float(input())

# Every animal's food is in kilograms except for the turtle - its is in grams.

dog_food_total = days_out * dog_food

cat_food_total = days_out * cat_food

turtle_food_total = (days_out * turtle_food) / 1000

food_needed = dog_food_total + cat_food_total + turtle_food_total

if food >= food_needed:
    food_left = math.floor(food - food_needed)
    print(f"{food_left} kilos of food left.")
else:
    food_deficient = math.ceil(food_needed - food)
    print(f"{food_deficient} more kilos of food are needed.")
