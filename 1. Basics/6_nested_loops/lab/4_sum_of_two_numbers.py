start = int(input())
end = int(input())

special_number = int(input())

counter = 0

combination_successful = False

for x in range(start, end + 1):
    for y in range(start, end + 1):
        counter += 1

        if x + y == special_number:
            combination_successful = True
            break

    if combination_successful:
        print(f"Combination N:{counter}")
        print(f"{x} + {y} = {special_number}")

if not combination_successful:
    print(f"{counter} combinations - neither equals {special_number}")
