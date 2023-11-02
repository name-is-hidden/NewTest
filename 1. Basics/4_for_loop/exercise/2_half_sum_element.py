import sys

number = int(input())

max_number = -sys.maxsize
numbers_sum = 0

for numbers in range(number):
    current_number = int(input())
    numbers_sum += current_number

    if current_number > max_number:
        max_number = current_number

if max_number == numbers_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")

else:
    numbers_sum -= max_number           # taking the sum of the rest elements
    print("No")
    print(f"Diff = {abs(max_number - numbers_sum)}")
