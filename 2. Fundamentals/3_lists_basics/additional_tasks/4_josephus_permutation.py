input_integers = [int(x) for x in input().split()]
target = int(input())

new_list = list()
counter = 0
index = 0

while input_integers:
    counter += 1

    if counter % target == 0:
        new_list.append(input_integers.pop(index))

    else:
        index += 1

    if index >= len(input_integers):
        index = 0

print(str(new_list).replace(" ", ""))
