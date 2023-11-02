input_names = input().split(", ")

print(sorted(input_names, key=lambda name: (-len(name), name)))

#################################################################################################################

# input_names = input().split(", ")

# sorted_names = sorted(input_names)
# sorted_names = sorted(sorted_names, key=lambda name: (-len(name)))

# print(sorted_names)
