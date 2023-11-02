number_range = int(input())

positive_numbers = list()           # 0 (zero) is included in the positive numbers
negative_numbers = list()

for _ in range(number_range):
    current_number = int(input())

    if current_number < 0:
        negative_numbers.append(current_number)

    else:
        positive_numbers.append(current_number)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
