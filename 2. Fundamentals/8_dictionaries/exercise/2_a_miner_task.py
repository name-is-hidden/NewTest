command = input()

metals_list = list()

while command != 'stop':

    item = command
    metals_list.append(item)

    command = input()

metals_dict = dict()

for i in range(0, len(metals_list), 2):
    key = metals_list[i]
    value = int(metals_list[i + 1])

    if key not in metals_dict:
        metals_dict[key] = 0

    metals_dict[key] += value

for key, value in metals_dict.items():

    print(f'{key} -> {value}')
