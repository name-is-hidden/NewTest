numbers = int(input())

numbers_sum = 0

for number in range(numbers):
    current_number = int(input())

    numbers_sum += current_number

average_number = numbers_sum / numbers

print(f"{average_number:.2f}")
