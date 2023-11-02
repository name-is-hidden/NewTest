integers_input = [int(x) for x in input().split(", ")]

for number in integers_input:
    if number == 0:
        integers_input.remove(number)
        integers_input.append(0)

print(integers_input)
