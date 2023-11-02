input_numbers = [float(x) for x in input().split()]

each_number_count = dict()

for number in input_numbers:
    if number not in each_number_count:
        each_number_count[number] = 0

    each_number_count[number] += 1

for number, count in each_number_count.items():
    print(f"{number} - {count} times")
