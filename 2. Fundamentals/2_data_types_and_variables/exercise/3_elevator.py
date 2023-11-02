# import math

number_of_people = int(input())
elevator_capacity = int(input())

courses = 0

if number_of_people <= elevator_capacity:
    courses = 1

else:
    courses = int(number_of_people / elevator_capacity)

    if number_of_people % elevator_capacity != 0:
        courses += 1


# courses = math.ceil(number_of_people / elevator_capacity) - This is another way to go

print(courses)
