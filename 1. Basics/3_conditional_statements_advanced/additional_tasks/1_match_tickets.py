# vip ticket price = 499.99lv
# normal ticket price - 249.99lv

budget = float(input())
category = input()
people = int(input())

ticket_price = 0
transport = 0

# transport costs depend on the people amount:
# between 1 and 4 - 75% of the budget
# between 5 and 9 - 60% of the budget
# between 10 and 24 - 50% of the budget
# between 25 and 46 - 40% of the budget
# above 50 - 25% of the budget

if category == "VIP":
    ticket_price = 499.99

elif category == "Normal":
    ticket_price = 249.99

price = ticket_price * people

if 1 <= people <= 4:
    transport = 0.75 * budget

elif 5 <= people <= 9:
    transport = 0.6 * budget

elif 10 <= people <= 24:
    transport = 0.5 * budget

elif 25 <= people <= 49:
    transport = 0.4 * budget

elif people >= 50:
    transport = 0.25 * budget

total_price = transport + price

if budget >= total_price:
    left = budget - total_price
    print(f"Yes! You have {left:.2f} leva left.")

else:
    needed = total_price - budget
    print(f"Not enough money! You need {needed:.2f} leva.")
