rows_count = int(input())

result = list()

for _ in range(rows_count):
    row = [int(x) for x in input().split(", ")]

    result.append(
        [int(x) for x in row if x % 2 == 0]
    )
print(result)
