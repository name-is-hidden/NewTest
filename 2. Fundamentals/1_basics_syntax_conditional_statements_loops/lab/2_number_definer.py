input_number = float(input())

if input_number == 0:
    print("zero")

if input_number > 0:

    if 0 < input_number < 1:
        print("small positive")

    elif input_number > 1000000:
        print("large positive")

    else:
        print("positive")

if input_number < 0:

    if 0 > input_number > -1:
        print("small negative")

    elif input_number < -1000000:
        print("large negative")

    else:
        print("negative")
