number_of_lines = int(input())

water_tank_capacity = 0

for _ in range(number_of_lines):
    water_added = int(input())

    if water_added + water_tank_capacity <= 255:            # 255 is the total capacity
        water_tank_capacity += water_added
        continue

    print("Insufficient capacity!")

print(water_tank_capacity)
