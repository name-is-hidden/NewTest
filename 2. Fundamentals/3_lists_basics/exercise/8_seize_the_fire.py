input_string = input().split("#")
water_amount = int(input())

effort = 0  # this is estimated to be 25% of each cells' value
cells_sum = 0

print("Cells:")

for element in input_string:
    fire_info = element.split(" = ")
    fire_type, cell_value = fire_info[0], int(fire_info[1])

    if water_amount >= cell_value:
        if fire_type == "High" and 81 <= cell_value <= 125:
            water_amount -= cell_value
            effort += (cell_value * 0.25)
            cells_sum += cell_value
            print(" -", cell_value)

        elif fire_type == "Medium" and 51 <= cell_value <= 80:
            water_amount -= cell_value
            effort += (cell_value * 0.25)
            cells_sum += cell_value
            print(" -", cell_value)

        elif fire_type == "Low" and 1 <= cell_value <= 50:
            water_amount -= cell_value
            effort += (cell_value * 0.25)
            cells_sum += cell_value
            print(" -", cell_value)

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {cells_sum}")

########################################################################################################################

# level_of_fire = input().split("#")
# temp_list = []
# water_available = int(input())
# effort = 0                        # this is estimated to be 25% of each cells' value
# final_list = []
# print("Cells:")
#
# for i in range(len(level_of_fire)):
#     temp_list.append(level_of_fire[i].split())
#     conditions = [
#         temp_list[i][0] in "High" and 81 <= int(temp_list[i][2]) <= 125,
#         temp_list[i][0] in "Medium" and 51 <= int(temp_list[i][2]) <= 80,
#         temp_list[i][0] in "Low" and 1 <= int(temp_list[i][2]) <= 50
#     ]
#
#     if water_available >= int(temp_list[i][2]):
#         if any(conditions):
#             water_available -= int(temp_list[i][2])
#             effort += int(temp_list[i][2]) * 0.25
#             final_list.append(int(temp_list[i][2]))
#             print(f"- {temp_list[i][2]}")
#     else:
#         continue
#
# print(f"Effort: {effort:.2f}\nTotal Fire: {sum(final_list)}")
