# Write a program that calculates the perimeter and are ofa circle:

from math import pi

radius = float(input())

circle_perimeter = 2 * radius * pi      # Perimeter formula

circle_area = (radius ** 2) * pi        # Area formula

print(f"{circle_area:.2f}")
print(f"{circle_perimeter:.2f}")
