budget = float(input())
season = input()

destination = ""
place = ""
expenses = 0

# expenses are:
# if the destination is Bulgaria and the budget is 100lv or less:
# summer: 30% from budget / winter: 70% from budget
# if the destination is somewhere around the Balkans and the budget is 1000lv or less:
# summer: 40% from budget / winter: 80% from budget
# if the destination is somewhere around Europe and the budget is above 1000lv:
# regardless the season: 90% of budget

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        place = "Camp"
        expenses -= budget * 0.3

    elif season == "winter":
        place = "Hotel"
        expenses -= budget * 0.7

elif budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        place = "Camp"
        expenses -= budget * 0.4

    elif season == "winter":
        place = "Hotel"
        expenses -= budget * 0.8

elif budget > 1000:
    destination = "Europe"
    place = "Hotel"

    if season == "summer" or season == "winter":
        expenses -= budget * 0.9

print(f"Somewhere in {destination}")
print(f"{place} - {abs(expenses):.2f}")
