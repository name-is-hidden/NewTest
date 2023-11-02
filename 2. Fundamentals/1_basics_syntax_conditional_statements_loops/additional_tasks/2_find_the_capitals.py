input_string = input()

indices_list = list()

for i in range(len(input_string)):              # "i" is the position of the character
    if input_string[i].isupper():
        indices_list.append(i)

print(indices_list)
