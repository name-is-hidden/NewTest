budget = int(input())
season = input()
people = int(input())

rent = 0

# The rent of the boat during spring is 3000lv
# The rent of the boat during summer and autumn is 4200lv
# The rent of the boat during winter is 2600lv

# If the group consists of 6 people or fewer the discount is 10%
# If the group consists between 7 and 11 people the discount is 15%
# If the group consists of 12 people or more the discount is 25%
# The get additional discount if their group is even number, except for autumn. This discount applies after previous

if season == "Spring":
    rent = 3000
    if people <= 6:
        rent -= rent * 0.1
    elif 7 <= people <= 11:
        rent -= rent * 0.15
    elif people >= 12:
        rent -= rent * 0.25

elif season == "Summer":
    rent = 4200
    if people <= 6:
        rent -= rent * 0.1
    elif 7 <= people <= 11:
        rent -= rent * 0.15
    elif people >= 12:
        rent -= rent * 0.25

elif season == "Autumn":
    rent = 4200
    if people <= 6:
        rent -= rent * 0.1
    elif 7 <= people <= 11:
        rent -= rent * 0.15
    elif people >= 12:
        rent -= rent * 0.25

elif season == "Winter":
    rent = 2600
    if people <= 6:
        rent -= rent * 0.1
    elif 7 <= people <= 11:
        rent -= rent * 0.15
    elif people >= 12:
        rent -= rent * 0.25

if people % 2 == 0:
    if season == "Spring" \
            or season == "Summer" \
            or season == "Winter":
        rent -= rent * 0.05

if budget >= rent:
    money_left = budget - rent
    print(f"Yes! You have {money_left:.2f} leva left.")

else:
    money_needed = rent - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
