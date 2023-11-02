input_numbers = input().split()
input_numbers_list = list()

for number in input_numbers:
    current_number = round(float(number))
    input_numbers_list.append(current_number)

print(input_numbers_list)
