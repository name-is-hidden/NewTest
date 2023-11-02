import math

tournaments_count = int(input())
initial_points = int(input())

points = 0
wins = 0

total_points = 0
average = 0
wins_percentage = 0

for tournaments in range(tournaments_count):
    qualification = input()

    if qualification == "W":
        points += 2000                          # 2000 points are awarded to winners
        wins += 1

    elif qualification == "F":
        points += 1200                          # 1200 points are awarded to finalists

    elif qualification == "SF":
        points += 720                           # 720 points are awarded to semi - finalists.

    total_points = initial_points + points

    average = points / tournaments_count

    wins_percentage = wins / tournaments_count * 100

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average)}")
print(f"{wins_percentage:.2f}%")
