fruit = input()
weekday = input()
amount = float(input())

weekday_is_valid = True
fruit_is_valid = True

price = 0

if weekday == "Monday" \
        or weekday == "Tuesday" \
        or weekday == "Wednesday" \
        or weekday == "Thursday" \
        or weekday == "Friday":

    if fruit == "banana":
        price = 2.50

    elif fruit == "apple":
        price = 1.20

    elif fruit == "orange":
        price = 0.85

    elif fruit == "grapefruit":
        price = 1.45

    elif fruit == "kiwi":
        price = 2.70

    elif fruit == "pineapple":
        price = 5.50

    elif fruit == "grapes":
        price = 3.85

    else:
        fruit_is_valid = False

elif weekday == "Saturday" \
        or weekday == "Sunday":

    if fruit == "banana":
        price = 2.70

    elif fruit == "apple":
        price = 1.25

    elif fruit == "orange":
        price = 0.90

    elif fruit == "grapefruit":
        price = 1.60

    elif fruit == "kiwi":
        price = 3.00

    elif fruit == "pineapple":
        price = 5.60

    elif fruit == "grapes":
        price = 4.20

    else:
        fruit_is_valid = False

else:
    weekday_is_valid = False

if weekday_is_valid and fruit_is_valid:
    price *= amount
    print(f"{price:.2f}")

else:
    print("error")
