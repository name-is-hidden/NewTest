initial_energy = int(input())
command = input()
battles_won = 0

while command != "End of battle":
    enemy_distance = int(command)

    if initial_energy >= enemy_distance:
        initial_energy -= enemy_distance
        battles_won += 1

        if battles_won % 3 == 0:
            initial_energy += battles_won

    else:
        print(f"Not enough energy! Game ends with {battles_won} won battles and {initial_energy} energy")
        break

    command = input()

if command == "End of battle":
    print(f"Won battles: {battles_won}. Energy left: {initial_energy}")
