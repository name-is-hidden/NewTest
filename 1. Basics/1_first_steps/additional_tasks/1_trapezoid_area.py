# Write a program that calculates the area of a trapezoid

side_a = int(input())
side_b = int(input())
side_h = int(input())

trapezoid_area = (side_a + side_b) * side_h / 2

print(f"{trapezoid_area:.2f}")          # the result has to be formatted to the second decimal number
