names_count = int(input())

names_list = list()

for name in range(names_count):
    current_name = input()

    names_list.append(current_name)

set_of_names = set(names_list)

for name in set_of_names:
    print(name)

########################################################################################################################

# names = set(input() for _ in range(int(input())))
#
# [print(name) for name in names]
