input_number = int(input())

# If given number different from 0, positive in this case
if input_number > 0:

    # Iterate from 2 to n / 2
    for i in range(2, input_number // 2 + 1):

        # If input)number is divisible by any number between 2 and input_number / 2, it is not prime

        if (input_number % i) == 0:
            print(False)                # False means the number is not Prime
            break
    else:
        print(True)                     # True means the number is prime

else:
    print(False)
