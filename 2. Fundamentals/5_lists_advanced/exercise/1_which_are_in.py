first_list = input().split(", ")
second_list = input()

result_list = list(x for x in first_list if x in second_list)

print(result_list)
