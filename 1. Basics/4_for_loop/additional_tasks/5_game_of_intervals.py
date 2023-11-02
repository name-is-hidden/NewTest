game_duration = int(input())

first_interval = 0
second_interval = 0
third_interval = 0
fourth_interval = 0
fifth_interval = 0
invalid_numbers = 0

end_result = 0          # this variable will help calculate the average_result

for number in range(game_duration):
    current_number = int(input())

    # this is the first_interval
    if 0 == current_number <= 9:
        first_interval += 1
        end_result += current_number * 0.2  # if the number is in this range, we add 20% of it to the end result

    # this is the second_interval
    elif 10 <= current_number <= 19:
        second_interval += 1
        end_result += current_number * 0.3      # 30%

    # this is the third_interval
    elif 20 <= current_number <= 29:
        third_interval += 1
        end_result += current_number * 0.4      # 40%

    # this is the fourth_interval
    elif 30 <= current_number <= 39:
        fourth_interval += 1
        end_result += 50                        # 50 points not percentage

    # this is the fifth_interval
    elif 40 <= current_number <= 50:
        fifth_interval += 1
        end_result += 100                       # 100 points not percentage

    # these are the invalid numbers - negative or above 50 / 0 > current_number or 50 < current_number /
    else:
        invalid_numbers += 1
        end_result /= 2

print(f'{end_result:.2f}')
print(f'From 0 to 9: {(first_interval / game_duration * 100):.2f}%')
print(f'From 10 to 19: {(second_interval / game_duration * 100):.2f}%')
print(f'From 20 to 29: {(third_interval / game_duration * 100):.2f}%')
print(f'From 30 to 39: {(fourth_interval / game_duration * 100):.2f}%')
print(f'From 40 to 50: {(fifth_interval / game_duration * 100):.2f}%')
print(f'Invalid numbers: {(invalid_numbers / game_duration * 100):.2f}%')
