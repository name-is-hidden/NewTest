# every new input number (real number) must be multiplied by 2 only positive or 0

number = float(input())

while True:
    if number < 0:
        print("Negative number!")
        break

    else:
        print(f"Result: {number * 2:.2f}")

    number = float(input())
