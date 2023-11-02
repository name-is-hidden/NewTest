message = input()
command = input()

while command != "Decode":
    command_parameter = command.split("|")

    if command_parameter[0] == "Move":
        location = int(command_parameter[1])
        movement = message[:location]
        static = message[location:]

        message = static + movement

    elif command_parameter[0] == "Insert":
        index = int(command_parameter[1])
        value = command_parameter[2]

        before = message[:index]
        after = message[index:]

        message = before + value + after

    elif command_parameter[0] == "ChangeAll":
        current_substring = command_parameter[1]
        replacement_string = command_parameter[2]

        message = message.replace(current_substring, replacement_string)

    command = input()

print(f"The decrypted message is: {message}")
