command = input()

secret_phrase = ""
met_letters = ""
result = ""

while command != "End":

    if command == "c" and command not in met_letters:
        met_letters += command

    elif command == "o" and command not in met_letters:
        met_letters += command

    elif command == "n" and command not in met_letters:
        met_letters += command

    else:

        if command.isalpha():
            secret_phrase += command

    if len(met_letters) == 3:
        secret_phrase += " "
        met_letters = ""
        result += secret_phrase
        secret_phrase = ""

    command = input()

print(result)
