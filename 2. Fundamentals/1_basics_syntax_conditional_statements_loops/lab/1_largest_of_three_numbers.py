first_number = int(input())
second_number = int(input())
third_number = int(input())

if first_number > second_number and first_number > third_number:
    print(first_number)

elif second_number > first_number and second_number > third_number:
    print(second_number)

else:
    print(third_number)

# OR:

# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
# largest_number = 0
#
# if first_number > second_number and first_number > third_number:
#     largest_number = first_number
#
# elif second_number > first_number and second_number > third_number:
#     largest_number = second_number
#
# else:
#     largest_number = third_number
#
# print(largest_number)
