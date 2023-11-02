dishwasher_diluent_count = int(input())

diluent_total = dishwasher_diluent_count * 750          # 750ml. is the volume of 1 bottle

dish_diluent = 5                                        # 5ml. are used to wash a single dish
pot_diluent = 15                                        # 15ml. are used to wash a single pot

dish_total = 0
pot_total = 0

counter = 0                                             # Every 3rd loading of the dishwasher is with pots

command = input()

diluent_is_enough = False

while command != "End":
    utensils_amount = int(command)
    counter += 1

    if counter % 3 == 0:
        pot_total += utensils_amount
        diluent_total -= utensils_amount * pot_diluent

    else:
        dish_total += utensils_amount
        diluent_total -= utensils_amount * dish_diluent

    if diluent_total >= 0:
        diluent_is_enough = True

    else:
        diluent_is_enough = False
        print(f"Not enough detergent, {abs(diluent_total)} ml. more necessary!")
        break

    command = input()

if diluent_is_enough:
    print("Detergent was enough!")
    print(f"{dish_total} dishes and {pot_total} pots were washed.")
    print(f"Leftover detergent {diluent_total} ml.")
