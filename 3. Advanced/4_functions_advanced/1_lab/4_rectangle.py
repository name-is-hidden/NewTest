def rectangle(a, b):
    def area():
        return a * b

    def perimeter():
        return 2 * (a + b)

    if not isinstance(a, int) \
            or not isinstance(b, int):
        return "Enter valid values!"

    return f"""Rectangle area: {area()}
Rectangle perimeter: {perimeter()}"""
