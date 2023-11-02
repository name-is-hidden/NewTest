first = int(input())
second = int(input())

for numbers in range(first, second + 1):
    current_number = str(numbers)

    odd_sum = 0
    even_sum = 0

    for index, digit in enumerate(current_number):

        if index % 2 == 0:
            even_sum += int(digit)

        else:
            odd_sum += int(digit)

    if odd_sum == even_sum:
        print(numbers, end=" ")
