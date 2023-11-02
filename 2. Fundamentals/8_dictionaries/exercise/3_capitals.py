# countries = input().split(', ')
# cities = input().split(', ')

capital_cities = dict(zip((countries for countries in input().split(', ')), (cities for cities in input().split(', '))))

for countries, cities in capital_cities.items():
    print(f'{countries} -> {cities}')
