# flower prices depend on the season:
# during spring or summer:
# Chrysanthemum - 2.00lv
# Rose - 4.10lv
# Tulip - 2.50lv.

# during autumn or winter:
# Chrysanthemum - 3.75lv
# Rose - 4.50lv
# Tulip - 4.15lv

chrysanthemums_amount = int(input())
roses_amount = int(input())
tulips_amount = int(input())
season = input()
day_type = input()               # Y for non-working day and N for working day

# during holidays, prices increase by 15%

chrysanthemum_price = 0
rose_price = 0
tulip_price = 0

# discounts are applicable:
# for more than 7 tulips during spring - 5% of the final price
# for 10 roses or above during winter - 10% of the final price
# for more than 20 flowers, regardless the season - 20% of the final price

# building the bouquet costs 2

if season == "Spring" or season == "Summer":
    chrysanthemum_price = 2.00
    rose_price = 4.10
    tulip_price = 2.50

elif season == "Autumn" or season == "Winter":
    chrysanthemum_price = 3.75
    rose_price = 4.50
    tulip_price = 4.15

chrysanthemums = chrysanthemums_amount * chrysanthemum_price

roses = roses_amount * rose_price

tulips = tulips_amount * tulip_price

total_price = chrysanthemums + roses + tulips

if day_type == "Y":
    total_price += total_price * 0.15


if season == "Spring" and tulips_amount > 7:
    total_price -= total_price * 0.05

if season == "Winter" and roses_amount >= 10:
    total_price -= total_price * 0.1

if chrysanthemums_amount + roses_amount + tulips_amount >= 20:
    total_price -= total_price * 0.2

bouquet = total_price + 2

print(f"{bouquet:.2f}")
