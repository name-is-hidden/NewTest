# prices are:
# during May and October:
# 50lv for studio and 65lv for apartment per night
# during June and September:
# 75.2lv for studio and 68.7lv for apartment per night
# during July and August:
# 76lv for studio and 77lv for apartment per night

month = input()
stay_amount = int(input())

studio = 0
apartment = 0

studio_total = 0
apartment_total = 0

# discounts are:
# for studio, for more than 7 nights during May and October - 5%
# for studio, for more than 14 nights during May and October - 30%
# for studio, for more than 14 nights during June and September - 20%
# for apartment for more than 14 nights, regardless the month - 10%

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    studio_total = studio * stay_amount
    apartment_total = apartment * stay_amount

    if 7 < stay_amount < 14:
        studio -= studio * 0.05
        studio_total = studio * stay_amount

    elif stay_amount > 14:
        studio -= studio * 0.3
        apartment -= apartment * 0.1
        studio_total = studio * stay_amount
        apartment_total = apartment * stay_amount

elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.70
    studio_total = studio * stay_amount
    apartment_total = apartment * stay_amount

    if stay_amount > 14:
        studio -= studio * 0.2
        apartment -= apartment * 0.1
        studio_total = studio * stay_amount
        apartment_total = apartment * stay_amount

elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    studio_total = studio * stay_amount
    apartment_total = apartment * stay_amount

    if stay_amount > 14:
        apartment -= apartment * 0.1
        apartment_total = apartment * stay_amount

print(f"Apartment: {apartment_total:.2f} lv.")
print(f"Studio: {studio_total:.2f} lv.")
