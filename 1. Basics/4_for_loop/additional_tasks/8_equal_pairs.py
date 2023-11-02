import sys

numbers_count = int(input())

sum_of_pair = 0  # The sum of a pair

difference = -sys.maxsize

are_different = False

for number in range(numbers_count):
    first_pair = int(input())
    second_pair = int(input())

    current_sum = first_pair + second_pair

    if number == 0:
        sum_of_pair = current_sum

    else:
        if sum_of_pair != current_sum:
            difference = abs(sum_of_pair - current_sum)
            are_different = True
            sum_of_pair = current_sum

if are_different:
    print(f"No, maxdiff={difference}")

else:
    print(f"Yes, value={sum_of_pair}")
