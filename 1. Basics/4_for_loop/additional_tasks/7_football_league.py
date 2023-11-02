stadium_capacity = int(input())
fans_count = int(input())

a_sector = 0
b_sector = 0
v_sector = 0
g_sector = 0

for fan in range(fans_count):
    fan_sector = input()

    if fan_sector == "A":
        a_sector += 1

    elif fan_sector == "B":
        b_sector += 1

    elif fan_sector == "V":
        v_sector += 1

    elif fan_sector == "G":
        g_sector += 1

print(f"{(a_sector / fans_count * 100):.2f}%")
print(f"{(b_sector / fans_count * 100):.2f}%")
print(f"{(v_sector / fans_count * 100):.2f}%")
print(f"{(g_sector / fans_count * 100):.2f}%")
print(f"{(fans_count / stadium_capacity * 100):.2f}%")
