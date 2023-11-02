numbers = list(map(int, input().split()))
target = int(input())

iterations = 0
summation_pairs = set()

for main_index in range(len(numbers)):
    for secondary_index in range(main_index + 1, len(numbers)):
        iterations += 1

        if numbers[main_index] + numbers[secondary_index] == target:
            current_summation_pair = (numbers[main_index], numbers[secondary_index])
            print(f"{numbers[main_index]} + {numbers[secondary_index]} = {target}")
            summation_pairs.add(current_summation_pair)

print(f"Iterations done: {iterations}")

for pair in summation_pairs:
    print(pair)
