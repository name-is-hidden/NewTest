import re

text = input()

search_word = input()

expression = rf"\b{search_word}\b"

matches = re.findall(expression, text, re.IGNORECASE)

output = list()

for match in matches:
    output.append(match)

print(len(output))
