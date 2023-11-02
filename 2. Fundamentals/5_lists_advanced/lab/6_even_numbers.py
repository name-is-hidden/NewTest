input_numbers = list(map(int, input().split(", ")))

indices_list = list()

for number in range(len(input_numbers)):
    if input_numbers[number] % 2 == 0:
        indices_list.append(number)

print(indices_list)
