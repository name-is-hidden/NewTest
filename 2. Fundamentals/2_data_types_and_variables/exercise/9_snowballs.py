import sys

number_of_snowballs = int(input())

highest_value_ball = -sys.maxsize

for _ in range(number_of_snowballs):
    weight = int(input())
    airborne_time = int(input())
    quality = int(input())

    value = (weight / airborne_time) ** quality

    if value > highest_value_ball:
        highest_value_ball = value

        print(f"{weight} : {airborne_time} = {int(highest_value_ball)} ({quality})")
