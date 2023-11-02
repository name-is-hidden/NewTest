gasoline = 2.22
diesel = 2.33
gas = 0.93

fuel_type = input()
fuel_amount = float(input())
club_card = input()

total = 0

if club_card == "Yes":          # If the customer has club card there are fuel discounts:
    gasoline -= 0.18
    diesel -= 0.12
    gas -= 0.08

else:
    pass

if fuel_type == "Gasoline":
    total = gasoline * fuel_amount

elif fuel_type == "Diesel":
    total = diesel * fuel_amount

elif fuel_type == "Gas":
    total = gas * fuel_amount

if 20 <= fuel_amount <= 25:         # There are discount depending on the amount of fuel
    total -= total * 0.08

elif fuel_amount > 25:
    total -= total * 0.10

print(f"{total:.2f} lv.")
