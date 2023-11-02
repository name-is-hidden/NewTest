locations = int(input())

for location in range(locations):
    average_gold_per_day = float(input())
    days = int(input())
    per_day_revenue = 0

    for days in range(1, days + 1):
        gold_per_day = float(input())
        per_day_revenue += gold_per_day
        average = per_day_revenue / days

    if average >= average_gold_per_day:
        print(f"Good job! Average gold per day: {average:.2f}.")

    else:
        print(f"You need {average_gold_per_day - average:.2f} gold.")
