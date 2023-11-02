# if budget is 100 or less:
# class is Economy:
# type is cabrio during summer and will cost 35% of the budget
# type is jeep during winter and will cost 65% of the budget

# if budget is more than 100 and less than 500:
# class is Compact:
# type is cabrio during summer and will cost 45% of the budget
# type is jeep during winter and will cost 80% of the budget

# if budget is more than 500:
# class is Luxury:
# type will be jeep regardless the season and will cost 90% of the budget

budget = float(input())
season = input()

car_class = " "
car_type = " "
car_price = 0

if budget <= 100:
    car_class = "Economy class"

    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 0.35

    elif season == "Winter":
        car_type = "Jeep"
        car_price = budget * 0.65

elif 100 < budget <= 500:
    car_class = "Compact class"

    if season == "Summer":
        car_type = "Cabrio"
        car_price = budget * 0.45

    elif season == "Winter":
        car_type = "Jeep"
        car_price = budget * 0.80

elif budget > 500:
    car_class = "Luxury class"
    car_type = "Jeep"
    car_price = budget * 0.9

print(car_class)
print(f"{car_type} - {car_price:.2f}")
