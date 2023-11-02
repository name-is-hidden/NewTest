input_numbers = [int(x) for x in input().split()]
numbers_to_remove = int(input())

sorted_list = sorted(input_numbers)[:numbers_to_remove]

for i in sorted_list:
    if i in input_numbers:
        input_numbers.remove(i)

print(", ".join(map(str, input_numbers)))
