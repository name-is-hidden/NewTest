input_numbers = list(map(int, input().split()))

line = input()

while line != "end":

    if line == "decrease":
        input_numbers = list(map(lambda x: x - 1, input_numbers))

    else:
        explode = line.split()
        command = explode[0]
        first_index = int(explode[1])
        second_index = int(explode[2])

        if command == "swap":
            input_numbers[first_index], input_numbers[second_index] = input_numbers[second_index], input_numbers[first_index]

        elif command == "multiply":
            input_numbers[first_index] = input_numbers[first_index] * input_numbers[second_index]

    line = input()

print(", ".join(map(str, input_numbers)))
