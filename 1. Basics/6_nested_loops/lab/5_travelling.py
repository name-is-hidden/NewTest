command = input()

while command != "End":
    destination = command
    budget = float(input())
    money = 0

    while money < budget:
        saved_money = float(input())
        money += saved_money

    print(f"Going to {destination}!")
    command = input()
