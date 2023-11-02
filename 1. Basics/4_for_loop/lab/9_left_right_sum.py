number = int(input())

left_sum = 0
right_sum = 0

for numbers in range(2 * number):
    current_number = int(input())

    if numbers < number:
        left_sum += current_number

    else:
        right_sum += current_number

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")

else:
    print(f"No, diff = {abs(left_sum - right_sum)}")
