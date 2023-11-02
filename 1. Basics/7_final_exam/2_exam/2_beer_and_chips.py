import math

football_fan_name = input()
budget = float(input())
beer_bottles = int(input())
chips_amount = int(input())

beer = 1.20
beers_total = beer_bottles * beer

chips = beers_total * 0.45
chips_total = chips_amount * chips

total_amount = beers_total + math.ceil(chips_total)

if total_amount <= budget:
    print(f"{football_fan_name} bought a snack and has {budget - total_amount:.2f} leva left.")

else:
    print(f"{football_fan_name} needs {total_amount - budget:.2f} more leva!")
