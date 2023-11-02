def palindrome_integers(numbers):

    for num in numbers:
        if num == num[::-1]:
            print(True)

        else:
            print(False)


input_numbers = input().split(", ")
palindrome_integers(input_numbers)
