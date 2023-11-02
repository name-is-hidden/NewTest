def fill_the_box(a, b, c, *args):
    volume = a * b * c
    result = 0

    for i in args:
        if i == "Finish":
            break

        else:
            if volume >= i:
                volume -= i

            else:
                i -= volume
                result += i
                volume = 0

    if result:
        return f"No more free space! You have {result} more cubes."

    else:
        return f"There is free space in the box. You could put {volume} more cubes."
