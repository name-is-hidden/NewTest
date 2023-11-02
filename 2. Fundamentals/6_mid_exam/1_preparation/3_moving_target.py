targets = list(map(int, input().split()))

line = input()

while line != "End":
    explode = line.split()

    command = explode[0]
    index = int(explode[1])
    value = int(explode[2])

    if command == "Shoot" and 0 <= index < len(targets):
        current_target = targets[index]
        current_target -= value

        if current_target <= 0:
            targets.pop(index)

        else:
            targets[index] = current_target

    elif command == "Add":
        if 0 <= index < len(targets):
            targets.index(index, value)

        else:
            print("Invalid placement!")

    elif command == "Strike":
        if index - value >= 0 and index + value < len(targets):
            targets = targets[:index - value] + targets[index + value + 1:]

        else:
            print("Strike missed!")

    line = input()

print("|".join(list(map(str, targets))))
