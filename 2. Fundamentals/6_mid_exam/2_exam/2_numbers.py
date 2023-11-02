input_numbers = [int(x) for x in input().split()]

line = input()

while line != "Finish":
    command = line.split()[0]
    value = int(line.split()[1])

    if command == "Add":
        input_numbers.append(value)

    elif command == "Remove":
        if value in input_numbers:
            input_numbers.remove(value)

    elif command == "Replace":
        if value in input_numbers:
            if len(line) > 1:
                replacement = line.split()[2]
                position = input_numbers.index(value)
                input_numbers.pop(position)
                input_numbers.insert(position, replacement)

    elif command == "Collapse":
        for nums in input_numbers:
            if value > nums:
                input_numbers.remove(nums)

    line = input()

print(" ".join([str(x) for x in input_numbers]))
