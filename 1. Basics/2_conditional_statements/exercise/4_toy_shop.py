# Write a program that sums the profit for a shop owner and based on it decides weather he / she can go on a vacation
# or not.

puzzle = 2.60
doll = 3.00
teddy = 4.10
minion = 8.20
truck = 2.00

holiday_price = float(input())

puzzles_amount = int(input())
dolls_amount = int(input())
teddies_amount = int(input())
minions_amount = int(input())
trucks_amount = int(input())

total_amount = puzzles_amount + dolls_amount + teddies_amount + minions_amount + trucks_amount

puzzles_price = puzzle * puzzles_amount

dolls_price = doll * dolls_amount

teddies_price = teddy * teddies_amount

minions_price = minion * minions_amount

trucks_price = truck * trucks_amount

total_price = puzzles_price + dolls_price + teddies_price + minions_price + trucks_price

if total_amount >= 50:
    total_price -= total_price * 0.25     # 25% discount if the total is 50 or above

rent = total_price * 0.1                  # rent price is 10% of the total price
money_left = total_price - rent

if money_left >= holiday_price:
    cash = money_left - holiday_price
    print(f"Yes! {cash:.2f} lv left.")

else:
    money_needed = holiday_price - money_left
    print(f"Not enough money! {money_needed:.2f} lv needed")
