# Write a program that calculates the number of desks that fit in the room,considering some conditions:

side_a = float(input()) * 100           # we convert the input data from cm to m
side_b = (float(input()) * 100) - 100   # is the width of the walking path

desks_a = side_a // 120                 # 120 is the length of one desk

desks_b = side_b // 70                  # 70 is the width of one desk

total_desks = (desks_a * desks_b) - 3   # 3 desks are lost because of the door and the teacher's desk

print(round(total_desks))
