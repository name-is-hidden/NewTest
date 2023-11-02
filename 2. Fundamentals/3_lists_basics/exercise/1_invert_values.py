input_string = input().split()

opposites_list = list()

for item in input_string:
    current_number = int(item)

    opposites_list.append(current_number * -1)

print(opposites_list)

#############################################################################################################

# print([-int(x) for x in input().split()])             This is list comprehension
