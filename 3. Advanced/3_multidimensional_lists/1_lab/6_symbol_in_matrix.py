rows_columns = int(input())
matrix = [list(input()) for _ in range(rows_columns)]
symbol = input()

is_found = False

for row in range(rows_columns):
    if is_found:
        break

    for column in range(rows_columns):
        if matrix[row][column] == symbol:
            is_found = True
            print(f"({row}, {column})")
            break

if not is_found:
    print(f"{symbol} does not occur in the matrix")
