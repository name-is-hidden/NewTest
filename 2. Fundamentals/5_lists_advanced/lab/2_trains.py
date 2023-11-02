wagons_count = int(input())

train = [0 for i in range(wagons_count)]

command = input()

while command != "End":

    command_list = command.split()

    if command_list[0] == "add":
        train[-1] += int(command_list[1])

    elif command_list[0] == "insert":
        position = int(command_list[1])
        train[position] += int(command_list[2])

    elif command_list[0] == "leave":
        position = int(command_list[1])
        train[position] -= int(command_list[2])

    command = input()

print(train)
