energy = 100
coins = 100

events_string = input().split("|")

day_completed = True

for event in events_string:
    day_data = event.split("-")
    action, value = day_data[0], int(day_data[1])

    if action == "rest":
        if energy + value > 100:
            value = 0

        energy += value
        print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")

    elif action == "order":  # The energy cost is 30
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")

        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {action}.")

        else:
            day_completed = False
            print(f"Closed! Cannot afford {action}.")
            break

if day_completed:
    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
