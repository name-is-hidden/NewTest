employees_capacity = [int(input()) for x in range(1, 4)]
student_count = int(input())
hours = 0

while student_count > 0:

    for num in range(len(employees_capacity)):
        if student_count == 0:
            break

        else:
            student_count -= int(employees_capacity[num])

    hours += 1

    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")
