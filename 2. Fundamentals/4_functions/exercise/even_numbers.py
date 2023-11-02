def check_even(number):
    if number % 2 == 0:
        return True

    return False


even_list = filter(check_even, list(map(int, input().split())))
print(list(even_list))

###############################################################################################################

# even_list = list(filter(lambda x: x % 2 == 0, list(map(int, input().split()))))
#
# print(even_list)

###############################################################################################################

# def even_numbers(sorted_numbers):
#
#     even_numbers_list = list()
#
#     for i in sorted_numbers:
#         if i % 2 == 0:
#             even_numbers_list.append(i)
#
#     print(even_numbers_list)
#
#
# input_numbers = map(int, input().split())
#
# even_numbers(input_numbers)
