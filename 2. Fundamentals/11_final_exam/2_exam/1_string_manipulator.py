text = input()

command = input()

while command != "End":
    command_parameter = command.split()

    action = command_parameter[0]

    if action == "Translate":
        character = command_parameter[1]
        replacement_character = command_parameter[2]

        text = text.replace(character, replacement_character)
        print(text)

    elif action == "Includes":
        substring = command_parameter[1]

        if substring in text:
            print(True)

        else:
            print(False)

    elif action == "Start":
        substring = command_parameter[1]

        if substring in text[:len(substring)]:
            print(True)

        else:
            print(False)

    elif action == "Lowercase":
        text = text.lower()
        print(text)

    elif action == "FindIndex":
        character = command_parameter[1]
        print(text.rfind(character))

    elif action == "Remove":
        start = int(command_parameter[1])
        count = int(command_parameter[2])
        final = start + count

        new_beginning = text[:start]
        new_ending = text[final:]
        text = new_beginning + new_ending
        print(text)

    command = input()
