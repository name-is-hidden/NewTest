import math

hours_required = int(input())
days = int(input())
overtime_workers_count = int(input())

# Employees need to do a training which is 10 % of days
# 1 work day is 8 hours
# Allowed overtime is 2 hrs per day

education_hours = days * 0.1

working_hours = (days - education_hours) * 8

overtime_duration = overtime_workers_count * 2 * days

total_time = math.floor(working_hours + overtime_duration)

if hours_required <= total_time:
    left = abs(hours_required - total_time)
    print(f"Yes!{left} hours left.")
else:
    needed = abs(total_time - hours_required)
    print(f"Not enough time!{needed} hours needed.")
