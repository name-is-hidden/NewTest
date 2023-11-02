# Write a program that calculates the cost of food delivery:

chicken = 10.35
fish = 12.40
veggie = 8.15
delivery = 2.50

chicken_amount = int(input())
fish_amount = int(input())
veggie_amount = int(input())

chicken_price = chicken * chicken_amount

fish_price = fish * fish_amount

veggie_price = veggie * veggie_amount

food_price = chicken_price + fish_price + veggie_price

desert = food_price * 0.2                   # The desert costs is 20% from the total cost of food

total_price = food_price + desert + delivery

print(total_price)
