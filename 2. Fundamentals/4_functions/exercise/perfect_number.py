def perfect_number(number):
    digits_sum = 0

    for digit in range(1, number):
        if number % digit == 0:
            digits_sum += digit

    if digits_sum == number:
        return print("We have a perfect number!")

    return print("It's not so perfect.")


input_number = int(input())

perfect_number(input_number)
