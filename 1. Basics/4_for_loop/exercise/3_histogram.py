number = int(input())

p_1 = 0
p_2 = 0
p_3 = 0
p_4 = 0
p_5 = 0

for numbers in range(number):
    current_number = int(input())

    if current_number < 200:
        p_1 += 1

    elif 200 <= current_number <= 399:
        p_2 += 1

    elif 400 <= current_number <= 599:
        p_3 += 1

    elif 600 <= current_number <= 799:
        p_4 += 1

    elif current_number >= 800:
        p_5 += 1

p_1_percent = p_1 / number * 100

p_2_percent = p_2 / number * 100

p_3_percent = p_3 / number * 100

p_4_percent = p_4 / number * 100

p_5_percent = p_5 / number * 100

print(f"{p_1_percent:.2f}%")
print(f"{p_2_percent:.2f}%")
print(f"{p_3_percent:.2f}%")
print(f"{p_4_percent:.2f}%")
print(f"{p_5_percent:.2f}%")
