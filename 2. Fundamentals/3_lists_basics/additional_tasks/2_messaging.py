input_integers = [int(x) for x in input().split()]
input_string = input()

integer_index = list()

for number in input_integers:
    digits_sum = 0

    for digit in str(number):
        digits_sum += int(digit)

    integer_index.append(digits_sum)

message = ""

for i in integer_index:
    if i > len(input_string):
        current_index = i % len(input_string)
        message += input_string[current_index]
        input_string = input_string.replace(input_string[current_index], "", 1)

    else:
        message += input_string[i]
        input_string = input_string.replace(input_string[i], "", 1)

print(message)
