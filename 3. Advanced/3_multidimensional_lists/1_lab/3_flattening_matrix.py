rows_count = int(input())

result = list()

for _ in range(rows_count):
    current_row = [int(x) for x in input().split(", ")]

    result.extend(current_row)

print(result)

########################################################################################################################
#
# rows_count = int(input())
#
# matrix = [map(int, input().split(", ")) for _ in range(rows_count)]
#
# flattened = [num for row in matrix for num in row]
#
# print(flattened)
