# Write a program that calculates the house repair cost:

side_x = float(input())
side_y = float(input())
side_h = float(input())

front_back_walls = (2 * (side_x * side_x)) - (1.2 * 2)     # both are squares

side_walls = (2 * (side_x * side_y)) - (2 * (1.5 * 1.5))   # both are rectangles

roof_side_walls = 2 * (side_x * side_y)                    # both are rectangles

roof_front_back_sides = 2 * ((side_x * side_h) / 2)        # both are triangles

green = (front_back_walls + side_walls) / 3.4              # green is the body

red = (roof_side_walls + roof_front_back_sides) / 4.3      # red is the roof

print(f"{green:.2f}")
print(f"{red:.2f}")
