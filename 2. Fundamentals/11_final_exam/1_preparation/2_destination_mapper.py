import re

text = input()

destinations_list = list()
travel_points = 0

expression = r"([=/])([A-Z][A-Za-z]{2,})\1"

matches = re.finditer(expression, text)

for match in matches:
    destinations_list.append(match.group(2))
    travel_points += len(match.group(2))

print(f"Destinations: {', '.join(destinations_list)}")
print(f"Travel Points: {travel_points}")
