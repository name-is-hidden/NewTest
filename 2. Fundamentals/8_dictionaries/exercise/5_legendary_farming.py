text = input()

legendary_weapons = {'shards': 'Shadowmourne', 'fragments': 'Valanyr', 'motes': 'Dragonwrath'}

legendary_materials = {'shards': 0, 'fragments': 0, 'motes': 0}

other_materials = dict()

is_obtained = False

while not is_obtained:
    items = text.split()

    for item in range(0, len(items), 2):
        if is_obtained:
            break

        material, quantity = items[item + 1].lower(), int(items[item])

        if material in legendary_materials:
            legendary_materials[material] += quantity

        else:
            if material not in other_materials:
                other_materials[material] = 0

            other_materials[material] += quantity

        for material, quantity in legendary_materials.items():
            if quantity >= 250:
                is_obtained = True
                legendary_materials[material] -= 250
                print(f'{legendary_weapons[material]} obtained!')
                break

    if is_obtained:
        break

    text = input()

for material, quantity in legendary_materials.items():
    print(f'{material}: {quantity}')

for key, value in other_materials.items():
    print(f'{key}: {value}')
