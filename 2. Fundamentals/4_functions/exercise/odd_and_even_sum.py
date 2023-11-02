def odd_even_sum(numbers):

    odd_sum = 0
    even_sum = 0

    for i in numbers:
        if i % 2 == 0:
            even_sum += i

        else:
            odd_sum += i

    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


input_number = map(int, list(input()))

odd_even_sum(input_number)
