rows, columns = [int(x) for x in input().split(", ")]

matrix = list()

for _ in range(rows):
    matrix.append(
        [int(x) for x in input().split()]
    )

result = [0] * columns

for row in range(rows):
    for column in range(columns):
        result[column] += matrix[row][column]

for element in result:
    print(element)
