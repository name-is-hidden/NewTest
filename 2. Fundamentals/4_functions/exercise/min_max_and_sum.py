def min_max_and_sum(numbers):

    print(f"The minimum number is {min(numbers)}")
    print(f"The maximum number is {max(numbers)}")
    print(f"The sum number is: {sum(numbers)}")

input_numbers = list(map(int, input().split()))

min_max_and_sum(input_numbers)

###########################################################################################

# # import sys
#
#
# def min_max_and_sum(numbers):
#     min_number = min(numbers)                   # # min_number = sys.maxsize
#     max_number = max(numbers)                   # # max_number = -sys.maxsize
#     sum_of_all_numbers = 0
#
#     for i in numbers:
#
#         # if i < min_number:
#         #     min_number = i
#         #
#         # if i > max_number:
#         #     max_number = i
#
#         sum_of_all_numbers += i
#
#     print(f"The minimum number is {min_number}")
#     print(f"The maximum number is {max_number}")
#     print(f"The sum number is: {sum_of_all_numbers}")
#
#
# import_numbers = list(map(int, input().split()))
#
# min_max_and_sum(import_numbers)
