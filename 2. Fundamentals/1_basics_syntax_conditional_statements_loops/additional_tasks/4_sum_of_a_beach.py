# Searched words are: beach = ["sand", "water", "fish", "sun"]

input_string = input().lower()

string_list = "".join(input_string)

sand = string_list.count("sand")
water = string_list.count("water")
fish = string_list.count("fish")
sun = string_list.count("sun")

result = sand + water + fish + sun

print(result)
