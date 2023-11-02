chat = list()
line = input()

while line != "end":
    command = line.split()[0]
    value = line.split()[1]

    if command == "Chat":
        chat.append(value)

    elif command == "Delete":
        if value in chat:
            chat.remove(value)
        else:
            pass

    elif command == "Edit":
        if value in chat:
            replacement = line.split()[2]
            position = chat.index(value)
            chat.remove(value)
            chat.insert(position, replacement)
        else:
            pass

    elif command == "Pin":
        if value in chat:
            chat.append(chat.pop(chat.index(value)))
        else:
            pass

    elif command == "Spam":
        for messages in line.split()[1:]:
            chat.append(messages)

    line = input()

print("\n".join([str(x) for x in chat]))
