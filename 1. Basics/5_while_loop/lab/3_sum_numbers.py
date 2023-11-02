number = int(input())
numbers_sum = 0

while number > numbers_sum:
    current_number = int(input())

    numbers_sum += current_number

if numbers_sum == number:
    print(number)

else:
    print(numbers_sum)
