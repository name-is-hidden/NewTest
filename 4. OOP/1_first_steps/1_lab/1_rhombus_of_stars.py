def get_line(i, n):
    spaces = n - 1 - i
    stars = i + 1

    return " " * spaces + "* " * stars


def print_rhombus(n):
    for i in range(n):
        print(get_line(i, n))

    for i in range(n - 2, -1, -1):
        print(get_line(i, n))


print_rhombus(1)
print_rhombus(2)
print_rhombus(3)
print_rhombus(4)
