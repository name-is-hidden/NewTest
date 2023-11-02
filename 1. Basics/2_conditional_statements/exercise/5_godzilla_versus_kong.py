# Write a program that calculates the expenses and checks whether the budget will be okay to start making a movie:

budget = float(input())
people_count = int(input())
costume_price = float(input())

decor_price = budget * 0.1     # decor costs 10% of the budget

if people_count >= 150:
    costume_price = costume_price - (costume_price * 0.1)     # 10% discount if people are 150 or above

costumes = people_count * costume_price

total_expenses = decor_price + costumes

if total_expenses > budget:
    money_needed = total_expenses - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")

else:
    money_left = budget - total_expenses
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
