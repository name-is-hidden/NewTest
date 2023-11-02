gifts = input().split()

while True:
    command = input().split()

    if command[0] == "OutOfStock":
        if command[1] in gifts:
            for gift in gifts:
                if gift == command[1]:
                    index = gifts.index(gift)
                    gifts.pop(index)
                    gifts.insert(index, "None")

    elif command[0] == "Required":
        replacement_index = int(command[2])

        if 0 <= replacement_index <= (len(gifts) - 1):
            gifts.pop(replacement_index)
            gifts.insert(replacement_index, command[1])

    elif command[0] == "JustInCase":
        gifts.remove(gifts[-1])
        gifts.append(command[1])

    else:
        break

for gift in gifts:
    if gift != "None":
        print(gift, end=" ")
