def sum_numbers(first_number, second_number):
    return first_number + second_number


def subtract(current_sum, third_number):
    return current_sum - third_number


a, b, c = int(input()), int(input()), int(input())

result = subtract(sum_numbers(a, b), c)

print(result)
