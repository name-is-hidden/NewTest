def operate(operation, *args):
    def add(*args):
        return sum(args)

    def subtract(x, *args):
        return x + sum(-y for y in args)

    def multiply(*args):
        result = 1

        for i in args:
            result *= i

        return result

    def divide(x, *args):
        result = x

        for value in args:
            result /= value

        return result

    if operation == "+":
        return add(*args)

    elif operation == "-":
        return subtract(*args)

    elif operation == "*":
        return multiply(*args)

    elif operation == "/":
        return divide(*args)
