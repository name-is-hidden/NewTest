age = int(input())
washing_machine = float(input())
toy_price = int(input())

money = 0                       # Lilly gets money for even birthdays
money_after_brother = 0         # Lilly's brother gets 1 BGN for every even birthday she has
toys = 0                        # Lilly gets toys for her odd birthdays

for birthdays in range(1, age + 1):
    if birthdays % 2 == 0:          # She starts from 10 and gets more each time, compared to previous
        money += 10
        money_after_brother += money - 1

    else:
        toys += 1

toys_total = toy_price * toys

total_money = toys_total + money_after_brother

if total_money >= washing_machine:
    left = total_money - washing_machine
    print(f"Yes! {left:.2f}")

else:
    needed = washing_machine - total_money
    print(f"No! {needed:.2f}")
