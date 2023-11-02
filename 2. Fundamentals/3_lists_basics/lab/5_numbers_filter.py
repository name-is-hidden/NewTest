numbers_range = int(input())

even = list()               # 0 (zero) counts as even number
odd = list()
positive = list()           # 0 (zero) counts as positive number
negative = list()

for _ in range(numbers_range):
    current_number = int(input())

    if current_number % 2 == 0:
        even.append(current_number)

    if current_number % 2 == 0:
        odd.append(current_number)

    if current_number >= 0:
        positive.append(current_number)

    if current_number < 0:
        negative.append(current_number)

command = input()

print(eval(command))
