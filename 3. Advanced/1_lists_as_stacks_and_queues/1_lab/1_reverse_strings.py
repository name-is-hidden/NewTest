input_string = input()
string_list = list()        # this is a stack

for item in input_string:
    string_list.append(item)        # push into the stack

reversed_string = ""

while string_list:
    value = string_list[-1]

    reversed_string += value
    string_list.pop()           # pop the last item of the stack

print(reversed_string)
