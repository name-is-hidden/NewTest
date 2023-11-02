# rose = 5
# dahlia = 3.80
# tulip = 2.80
# narcissus = 3
# gladiolus - 2.50

flower = input()
amount = int(input())
budget = int(input())

price = 0
discount = 0
total = 0

# If roses are more than 80 discount is 10%
# If dahlias are more than 90, discount is 15%
# If tulips are more than 80, discount is 15%
# If narcissuses are less than 120, prices increases by 15%
# IfGladiolus are less than 80, price increases by 20%

if flower == "Roses":
    price = 5
    total = price * amount
    if amount > 80:
        discount = 0.1
        total -= total * discount

elif flower == "Dahlias":
    price = 3.80
    total = price * amount
    if amount > 90:
        discount = 0.15
        total -= total * discount

elif flower == "Tulips":
    price = 2.80
    total = price * amount
    if amount > 80:
        discount = 0.15
        total -= total * discount

elif flower == "Narcissus":
    price = 3
    total = price * amount
    if amount < 120:
        discount = 0.15
        total += total * discount

elif flower == "Gladiolus":
    price = 2.50
    total = price * amount
    if amount < 80:
        discount = 0.2
        total += total * discount

if budget >= total:
    money_left = budget - total
    print(f"Hey, you have a great garden with {amount} {flower} and {money_left:.2f} leva left.")

else:
    money_needed = total - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")
