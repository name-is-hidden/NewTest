heroes_count = int(input())

heroes_dict = dict()

for hero in range(heroes_count):
    new_hero = input().split()

    hero_name = new_hero[0]
    health_points = int(new_hero[1])
    mana_points = int(new_hero[2])

    current_hero_dict = dict()
    current_hero_dict["HP"] = health_points
    current_hero_dict["MP"] = mana_points

    heroes_dict[hero_name] = current_hero_dict              # This creates a nested dictionary with both value types

command = input()

while command != "End":
    command_parameters = command.split(" - ")

    type_of_command = command_parameters[0]
    hero_name = command_parameters[1]
    value = int(command_parameters[2])

    if type_of_command == "CastSpell":
        spell = command_parameters[3]

        if heroes_dict[hero_name]["MP"] >= value:
            heroes_dict[hero_name]["MP"] -= value

            print(f"{hero_name} has successfully cast {spell} and now has {heroes_dict[hero_name]['MP']} MP!")

        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")

    elif type_of_command == "TakeDamage":
        attacker = command_parameters[3]
        heroes_dict[hero_name]["HP"] -= value

        if heroes_dict[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {value} HP by {attacker} and now has {heroes_dict[hero_name]['HP']} HP left!")

        else:
            heroes_dict.pop(hero_name)
            print(f"{hero_name} has been killed by {attacker}!")

    elif type_of_command == "Recharge":

        if heroes_dict[hero_name]["MP"] + value > 200:
            value = 200 - heroes_dict[hero_name]["MP"]
            heroes_dict[hero_name]["MP"] = 200

        else:
            heroes_dict[hero_name]["MP"] += value

        print(f"{hero_name} recharged for {value} MP!")

    elif type_of_command == "Heal":

        if heroes_dict[hero_name]["HP"] + value > 100:
            value = 100 - heroes_dict[hero_name]["HP"]
            heroes_dict[hero_name]["HP"] = 100

        else:
            heroes_dict[hero_name]["HP"] += value

        print(f"{hero_name} healed for {value} HP!")

    command = input()

for hero in heroes_dict:
    print(f"{hero}")

    print(f"  HP: {heroes_dict[hero]['HP']}")

    print(f"  MP: {heroes_dict[hero]['MP']}")
