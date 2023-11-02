trip_cost = float(input())
available_money = float(input())

spend_days = 0
days = 0

while True:
    action = input()
    money = float(input())
    days += 1

    if action == "spend":
        spend_days += 1
        available_money -= money

        if available_money < 0:
            available_money = 0

        if spend_days == 5:
            print("You can't save the money.")
            print(days)
            break

    else:
        spend_days = 0
        available_money += money

    if available_money >= trip_cost:
        print(f"You saved the money for {days} days.")
        break
