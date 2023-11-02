# Write a program that calculates the volume of a rectangular parallelepiped, after it is filled with equipment:
# 1 liter = 1 cubic decimeter

side_a = int(input())           # in centimeters
side_b = int(input())           # in centimeters
side_c = int(input())           # in centimeters

percent_occupied = float(input()) / 100             # in percent

volume = (side_a * side_b * side_c) / 1000          # in liters

liters_needed = volume * (1 - percent_occupied)

print(liters_needed)
