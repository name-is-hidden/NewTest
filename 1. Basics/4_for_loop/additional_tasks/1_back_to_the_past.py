inherited_money = float(input())
years_to_live = int(input())

current_age = 18

for year in range(1800, years_to_live + 1):

    if year % 2 == 0:
        inherited_money -= 12000                # He spends 12k when the year is even

    else:                                   # He spends 12k + 50 * his current age (starting from 18)
        inherited_money -= 12000 + (50 * current_age)

    current_age += 1

if inherited_money >= 0:
    print(f"Yes! He will live a carefree life and will have {inherited_money:.2f} dollars left.")

else:
    print(f"He will need {abs(inherited_money):.2f} dollars to survive.")
