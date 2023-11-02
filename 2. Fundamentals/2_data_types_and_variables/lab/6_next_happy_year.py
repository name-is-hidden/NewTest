year = int(input())

year_is_happy = False

while not year_is_happy:
    year += 1
    str_year = str(year)
    set_year = set()

    for digits in range(len(str_year)):
        set_year.add(str_year[digits])

    year_is_happy = len(str_year) == len(set_year)

print(year)
