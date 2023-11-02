clothes = [int(x) for x in input().split()]
rack_capacity = int(input())

current_rack = rack_capacity

racks_count = 1

while clothes:
    if clothes[-1] > current_rack:

        racks_count += 1
        current_rack = rack_capacity

    else:
        current_rack -= clothes[-1]
        clothes.pop()

print(racks_count)
