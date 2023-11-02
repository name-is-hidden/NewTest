limit_number = int(input())

for numbers in range(1, limit_number + 1):
    sum_of_digits = 0
    digits = numbers

    while digits > 0:
        sum_of_digits += digits % 10            # this way we will get the last digit of the number
        digits = int(digits / 10)               # this way we will get the first digit of the number

    if sum_of_digits == 5 or sum_of_digits == 7 or sum_of_digits == 11:
        print(f"{numbers} -> True")

    else:
        print(f"{numbers} -> False")
