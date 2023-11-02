import sys

numbers_count = int(input())

odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize

even_sum = 0
even_min = sys.maxsize
even_max = -sys.maxsize

for number in range(1, numbers_count + 1):
    current_number = float(input())

    if current_number == 0:
        odd_min, odd_max, even_min, even_max = "No", "No", "No", "No"

    if number % 2 == 0:
        even_sum += current_number

        if current_number < even_min:
            even_min = current_number

        if current_number > even_max:
            even_max = current_number

    else:
        odd_sum += current_number

        if current_number < odd_min:
            odd_min = current_number

        if current_number > odd_max:
            odd_max = current_number

print(f"OddSum={odd_sum:.2f},")
print(f"OddMin={odd_min:.2f},")
print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
print(f"EvenMin={even_min:.2f},")
print(f"EvenMax={even_max:.2f}")
