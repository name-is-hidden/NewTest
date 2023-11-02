# Seasons to choose are Summer and Winter
# Locations are Alaska and Morocco
# Places to stay are Hotel, Hut or Camp

# if budget is 1000 or less:
# place to stay is Camp
# if season is summer, location is Alaska and will cost 65% of budget
# if season is winter, location is Morocco and will cost 45% of budget

# if budget is more than 1000 but less than 3000:
# place to stay is Hut
# if season is summer, location is Alaska and will cost 80% of the budget
# if season is winter, location is Morocco and will ost 60% of the budget

# if budget is above 3000:
# place to stay is Hotel
# if season is summer, location is Alaska and will cost 90% of the budget
# if season is winter, location is Morocco and will cost 90% of the budget

budget = float(input())
season = input()

stay_price = 0
place = " "
place_to_stay = " "

if budget <= 1000:
    place = "Camp"
    if season == "Summer":
        place_to_stay = "Alaska"
        stay_price = budget * 0.65

    elif season == "Winter":
        place_to_stay = "Morocco"
        stay_price = budget * 0.45

elif 1000 < budget <= 3000:
    place = "Hut"
    if season == "Summer":
        place_to_stay = "Alaska"
        stay_price = budget * 0.80

    elif season == "Winter":
        place_to_stay = "Morocco"
        stay_price = budget * 0.60

elif budget > 3000:
    place = "Hotel"
    stay_price = budget * 0.90
    if season == "Summer":
        place_to_stay = "Alaska"

    elif season == "Winter":
        place_to_stay = "Morocco"

print(f"{place_to_stay} - {place} - {stay_price:.2f}")
