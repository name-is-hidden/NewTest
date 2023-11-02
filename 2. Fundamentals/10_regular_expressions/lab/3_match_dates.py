import re

text = input()

expression = r"(?P<date>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"

matches = re.finditer(expression, text)

for match in matches:
    day = match.group("date")
    month = match.group("month")
    year = match.group("year")

    print(f"Day: {day}, Month: {month}, Year: {year}")

########################################################################################################################

# import re
#
# expression = r"(?P<date>\d{2})(?P<separator>[./-])(?P<month>[A-Z][a-z]{2})\2(?P<year>\d{4})"
#
# text = input()
#
# matches = re.findall(expression, text)
#
# for match in matches:
#     date, month, year = match[0], match[2], match[3]
#     print(f"Day: {date}, Month: {month}, Year: {year}")
