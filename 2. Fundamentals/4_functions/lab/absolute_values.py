input_numbers = input().split()
absolute_numbers_list = list()

for number in input_numbers:
    current_number = abs(float(number))
    absolute_numbers_list.append(current_number)

print(absolute_numbers_list)
