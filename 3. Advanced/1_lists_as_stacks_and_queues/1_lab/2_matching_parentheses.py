expression = input()

string_list = list()         # this is a stack

for symbol in range(len(expression)):
    character = expression[symbol]

    if character == "(":
        string_list.append(symbol)

    elif character == ")":
        start = string_list.pop()
        end = symbol + 1
        print(expression[start:end])
