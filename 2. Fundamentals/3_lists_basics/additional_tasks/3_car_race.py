input_string = [int(x) for x in input().split()]

middle_index = (len(input_string) // 2)

# if there is a 0 in the list, the sum of all values must be reduced by 20%

right_half_list = input_string[:middle_index:-1]
left_half_list = input_string[:middle_index]

right_sum = 0

for x in right_half_list:
    if x == 0:
        right_sum *= 0.8

    right_sum += x

left_sum = 0

for y in left_half_list:
    if y == 0:
        left_sum *= 0.8

    left_sum += y

if right_sum < left_sum:
    print(f"The winner is right with total time: {right_sum:.1f}")

if left_sum < right_sum:
    print(f"The winner is left with total time: {left_sum:.1f}")
