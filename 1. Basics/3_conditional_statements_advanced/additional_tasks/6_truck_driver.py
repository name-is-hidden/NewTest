# His wage depends on the distance he has travelled and the season:
# during spring or autumn:
# for 5000km or less - 0.75lv per km
# between 5000km and 10000km - 0.95lv per km

# during summer:
# for 5000km or less - 0.90lv per km
# between 5000lv and 10000km - 1.10lv per km

# during winter:
# for 5000km or less - 1.05lv. per km
# between 5000km and 10000km - 1.25lv per km

# between 10000km and 20000km - 1.45lv per km REGARDLESS THE SEASON

season = input()
distance = float(input())

price_per_km = 0

if distance <= 5000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.75

    elif season == "Summer":
        price_per_km = 0.90

    elif season == "Winter":
        price_per_km = 1.05

elif 5000 < distance <= 10000:
    if season == "Spring" or season == "Autumn":
        price_per_km = 0.95

    elif season == "Summer":
        price_per_km = 1.10

    elif season == "Winter":
        price_per_km = 1.25

elif 10000 < distance <= 20000:
    price_per_km = 1.45

brutt_amount = 4 * (price_per_km * distance)
nett_amount = brutt_amount - (brutt_amount * 0.1)

print(f"{nett_amount:.2f}")
