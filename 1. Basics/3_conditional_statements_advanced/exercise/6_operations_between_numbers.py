a = int(input())
b = int(input())
operator = input()
result = 0

# allowed operators are: + - * / %

if operator == "+" or operator == "-" or operator == "*":

    if operator == "+":
        result = a + b
        if result % 2 == 0:
            print(f"{a} {operator} {b} = {result} - even")

        else:
            print(f"{a} {operator} {b} = {result} - odd")

    elif operator == "-":
        result = a - b
        if result % 2 == 0:
            print(f"{a} {operator} {b} = {result} - even")

        else:
            print(f"{a} {operator} {b} = {result} - odd")

    elif operator == "*":
        result = a * b
        if result % 2 == 0:
            print(f"{a} {operator} {b} = {result} - even")

        else:
            print(f"{a} {operator} {b} = {result} - odd")

elif operator == "/":
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result:.2f}")

    else:
        print(f"Cannot divide {a} by zero")

elif operator == "%":
    if b != 0:
        result = a % b
        print(f"{a} % {b} = {result}")

    else:
        print(f"Cannot divide {a} by zero")
