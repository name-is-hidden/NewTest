numbers_range = int(input())
filter_word = input()

full_list = list()
filtered_list = list()

for _ in range(numbers_range):
    current_string = input()

    full_list.append(current_string)

print(full_list)

for item in range(len(full_list)):
    filter_element = full_list[item]

    if filter_word in filter_element:
        filtered_list.append(filter_element)

print(filtered_list)
