import math

vines_area = int(input())
grapes_per_sqm = float(input())
wine_needed = int(input())                                 # quantity needed
workers_count = int(input())

total_grapes = vines_area * grapes_per_sqm

grapes_for_wine = total_grapes * 0.4                       # 40% of all grapes are used for wine

litres_wine = math.floor(round(grapes_for_wine / 2.5))     # 1l of wine requires 2.5kgs of grapes

if litres_wine < wine_needed:
    needed = abs(math.ceil(round(wine_needed - litres_wine)))
    print(f"It will be a tough winter! More {needed} litres wine needed.")

else:                                                       # if the wine exceeds the quantity needed it is split even between workers
    left = abs(math.ceil(round(wine_needed - litres_wine)))
    wine_per_worker = abs(math.ceil(round(left / workers_count)))
    print(f"Good harvest this year! Total wine: {litres_wine} liters.")
    print(f"{left} liters left -> {wine_per_worker} liters per person.")
    