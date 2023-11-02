# Write a program that reads a figure type and calculates and prints its area:

import math

figure = input()
side_a = float(input())
side_b = 0

if figure == "square":
    area = side_a * side_a
    print(f"{area:.3f}")

elif figure == "rectangle":
    side_b = float(input())
    area = side_a * side_b
    print(f"{area:.3f}")

elif figure == "circle":
    area = math.pi * (side_a ** 2)
    print(f"{area:.3f}")

elif figure == "triangle":
    side_b = float(input())
    area = side_a * side_b / 2
    print(f"{area:.3f}")
