import re

text = input()

expression = r"\b_[a-zA-Z0-9]+\b"

matches = re.findall(expression, text)

output = list()

for match in matches:
    output.append(match[1:])

print(",".join(output))
