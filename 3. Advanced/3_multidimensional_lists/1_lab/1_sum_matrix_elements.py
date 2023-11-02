rows, columns = [int(x) for x in input().split(", ")]

matrix = list()

for _ in range(rows):
    current_row = [int(x) for x in input().split(", ")]

    matrix.append(current_row)

result = 0

for item in range(len(matrix)):
    result += sum(matrix[item])

print(result)
print(matrix)
