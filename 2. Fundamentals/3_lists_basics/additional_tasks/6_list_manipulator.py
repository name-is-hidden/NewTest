import sys

numbers = [int(x) for x in input().split()]

while True:
    command = input().split()

    if command[0] == "exchange":
        index = int(command[1])

        if index < 0 or index + 1 > len(numbers):
            print("Invalid index")

        else:
            start_list = []
            end_list = []

            for x in numbers[index + 1:]:
                start_list.append(x)

            for x in numbers[:index + 1]:
                end_list.append(x)

            numbers.clear()
            numbers = start_list + end_list
            start_list.clear()
            end_list.clear()

    elif command[0] == "max":
        max_number = -sys.maxsize
        max_number_index = 0

        if command[1] == "even":
            for index, digit in enumerate(numbers):

                if digit % 2 == 0:
                    if digit >= max_number:
                        max_number = digit
                        max_number_index = index

        elif command[1] == "odd":
            for index, digit in enumerate(numbers):

                if digit % 2 != 0:
                    if digit >= max_number:
                        max_number = digit
                        max_number_index = index

        if max_number == -sys.maxsize:
            print("No matches")

        else:
            print(max_number_index)

    elif command[0] == "min":
        min_number = sys.maxsize
        min_number_index = 0

        if command[1] == "even":

            for index, digit in enumerate(numbers):
                if digit % 2 == 0:
                    if digit <= min_number:
                        min_number = digit
                        min_number_index = index

        elif command[1] == "odd":

            for index, digit in enumerate(numbers):
                if digit % 2 != 0:
                    if digit <= min_number:
                        min_number = digit
                        min_number_index = index

        if min_number == sys.maxsize:
            print("No matches")

        else:
            print(min_number_index)

    elif command[0] == "first":
        count = int(command[1])

        if count > len(numbers):
            print("Invalid count")

        else:
            first_list = []

            if command[2] == "even":

                for x in numbers:
                    if x % 2 == 0:
                        first_list.append(x)
                        if len(first_list) == count:
                            break

            elif command[2] == "odd":

                for x in numbers:
                    if x % 2 != 0:
                        first_list.append(x)

                        if len(first_list) == count:
                            break

            print(first_list)
            first_list.clear()

    elif command[0] == "last":
        count = int(command[1])

        if count > len(numbers):
            print("Invalid count")

        else:
            last_list = []
            numbers.reverse()

            if command[2] == "even":

                for x in numbers:
                    if x % 2 == 0:
                        last_list.append(x)
                        if len(last_list) == count:
                            break

            elif command[2] == "odd":

                for x in numbers:
                    if x % 2 != 0:
                        last_list.append(x)

                        if len(last_list) == count:
                            break

            last_list.reverse()
            print(last_list)
            last_list.clear()
            numbers.reverse()

    elif command[0] == "end":
        print(numbers)

        break
