quantity = int(input())
days_left = int(input())

# Decoration prices in USD per piece

ornament_set = 2
skirt = 5
garlands = 3
lights = 15

christmas_spirit = 0
cost = 0

for day in range(1, days_left + 1):
    if day % 2 == 0:                            # Every 2nd day you purchase an Ornament set
        christmas_spirit += 5
        cost += ornament_set * quantity

    if day % 3 == 0:                          # Every 3rd day you purchase Tree Skirts and Tree Garlands
        christmas_spirit += 13
        cost += (skirt + garlands) * quantity

    if day % 5 == 0:                          # Every 5th day you purchase Tree Lights
        christmas_spirit += 17
        cost += lights * quantity

        if day % 3 == 0:                        # If you have purchased Tree Skirts and Tree Garlands in this day, you have bonus spirit
            christmas_spirit += 30              # This can be done with a boolean variable as well

    if day % 10 == 0:                         # Every 10th day the cat ruins everything, and you purchase a skirt, garland and light
        christmas_spirit -= 20
        cost += skirt + garlands + lights

    if day % 11 == 0:                         # Every 11th day the quantity is increased by 2 because of the previous day
        quantity += 2

if days_left % 10 == 0:
    christmas_spirit -= 30

print(f"Total cost: {cost}")
print(f"Total spirit: {christmas_spirit}")
