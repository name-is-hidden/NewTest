input_number = int(input())

for numbers in range(input_number + 1):
    for others in range(numbers):
        print("*", end="")
    print()

for numbers in range(input_number - 1, -1, -1):
    for others in range(numbers):
        print("*", end="")
    print()
