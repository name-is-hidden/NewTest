input_string = input().split("|")
budget = int(input())

train_ticket = 150  # this is the price of the ticket

purchases_list = list()
earnings_list = list()  # 40% is the merge from the purchase cost (* 1.4)
money_spent = 0
is_enough = False

for element in input_string:
    purchase_info = element.split("->")
    clothing_type, price = purchase_info[0], float(purchase_info[1])

    if budget >= price:

        if clothing_type == "Clothes" and price <= 50:
            purchases_list.append(price)
            budget -= price
            money_spent += price

        elif clothing_type == "Shoes" and price <= 35:
            purchases_list.append(price)
            budget -= price
            money_spent += price

        elif clothing_type == "Accessories" and price <= 20.5:
            purchases_list.append(price)
            budget -= price
            money_spent += price

for price in purchases_list:
    earnings_list.append(price * 1.4)

for earning in earnings_list:
    print(f"{earning:.2f}", end=" ")

print()
print(f"Profit: {(sum(earnings_list) - money_spent):.2f}")

if (sum(earnings_list) + budget) >= train_ticket:
    print("Hello, France!")

else:
    print("Not enough money.")
