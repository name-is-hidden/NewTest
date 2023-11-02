cats_amount = int(input())

food = 12.45

group_1 = 0
group_2 = 0
group_3 = 0
total_food = 0

for cats in range(cats_amount):
    food_per_cat = float(input())
    total_food += food_per_cat

    if 100 <= food_per_cat < 200:
        group_1 += 1

    elif 200 <= food_per_cat < 300:
        group_2 += 1

    elif 300 <= food_per_cat < 400:
        group_3 += 1

print(f"Group 1: {group_1} cats.")
print(f"Group 2: {group_2} cats.")
print(f"Group 3: {group_3} cats.")
print(f"Price for food per day: {(total_food / 1000) * food:.2f} lv.")
