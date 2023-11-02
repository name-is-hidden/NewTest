input_numbers = list(map(int, input().split(", ")))

positive_numbers = [str(x) for x in input_numbers if x >= 0]
negative_numbers = [str(x) for x in input_numbers if x < 0]
even_numbers = [str(x) for x in input_numbers if x % 2 == 0]
odd_numbers = [str(x) for x in input_numbers if x % 2 != 0]

print(f"Positive: {', '.join(positive_numbers)}")
print(f"Negative: {', '.join(negative_numbers)}")
print(f"Even: {', '.join(even_numbers)}")
print(f"Odd: {', '.join(odd_numbers)}")

################################################################################################################

# input_numbers = list(map(int,input().split(", ")))
#
# positive = list()
# negative = list()
# even = list()
# odd = list()
#
# for number in input_numbers:
#     if number >= 0:
#         positive.append(number)
#
#     elif number < 0:
#         negative.append(number)
#
#     if number % 2 == 0:
#         even.append(number)
#
#     elif number % 2 != 0:
#         odd.append(number)
#
# print(f"Positive: {', '.join(positive_numbers)}")
# print(f"Negative: {', '.join(negative_numbers)}")
# print(f"Even: {', '.join(even_numbers)}")
# print(f"Odd: {', '.join(odd_numbers)}")
