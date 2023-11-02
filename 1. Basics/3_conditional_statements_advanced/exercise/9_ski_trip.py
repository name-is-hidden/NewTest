# room for one = 18.00
# apartment = 25.00
# president apartment = 35.00

days = int(input())
room_type = input()
remark = input()

nights = days - 1
total_price = nights * room_type
discount = 0

# discounts depend on room time and stay duration:
# room for one - doesn't have a discount regardless the duration
# apartment:
# for less than 10 days - 30% of the end price
# between 10 and 15 days - 35% of the end price
# for more than 15 days - 50% of the end price
# president apartment:
# for less than 10 days - 10% of the end price
# between 10 and 15 days - 15% of the end price
# for more than 15 days - 20% of the end price

if room_type == "room for one person":
    total_price = nights * 18.00

elif room_type == "apartment":
    total_price = nights * 25.00
    if days < 10:
        discount = 0.3
        total_price -= total_price * discount

    elif 10 <= days <= 15:
        discount = 0.35
        total_price -= total_price * discount

    elif days > 15:
        discount = 0.5
        total_price -= total_price * discount

elif room_type == "president apartment":
    total_price = nights * 35.00
    if days < 10:
        discount = 0.1
        total_price -= total_price * discount

    elif 10 <= days <= 15:
        discount = 0.15
        total_price -= total_price * discount

    elif days > 15:
        discount = 0.2
        total_price -= total_price * discount

if remark == "positive":
    total_price += total_price * 0.25

elif remark == "negative":
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")
