integers_string = [int(x) for x in input().split(", ")]     # using list comprehension we convert the strings into ints
beggars_count = int(input())

result = 0
result_list = list()

for beggar in range(beggars_count):
    for i in range(beggar, len(integers_string), beggars_count):
        result += integers_string[i]

    result_list.append(result)

    result = 0

print(result_list)
