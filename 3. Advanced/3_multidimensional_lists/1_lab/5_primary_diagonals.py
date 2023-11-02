rows = int(input())

matrix = list()

for _ in range(rows):
    matrix.append(
        [int(x) for x in input().split()]
    )

primary_diagonal_sum = 0

for x in range(len(matrix)):            # This is the formula to calculate the PRIMARY diagonal
    primary_diagonal_sum += matrix[x][x]              # Knowing that columns == rows

# primary_diagonal_sum = sum(matrix[i][i] for i in range(len(matrix)))

print(primary_diagonal_sum)

#######################################################################################################################

# Secondary diagonal formula:
# secondary_diagonal_sum = 0
#
# for x in range(len(matrix)):
#     secondary_diagonal_sum += matrix[x][len(matrix) - x - 1]
#
# # secondary_diagonal_sum = sum(matrix[i][len(matrix) - i - 1] for i in range(len(matrix
