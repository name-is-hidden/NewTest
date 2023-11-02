first_number, second_number = int(input()), int(input())

print("Before:")
print(f"a = {first_number}")
print(f"b = {second_number}")

first_number, second_number = second_number, first_number

print("After:")
print(f"a = {first_number}")
print(f"b = {second_number}")

# You can also swap the places e.g:
# a = second_number
# b = first_number
