import re

text = input()

username_expression = r"( |^)[a-zA-Z0-9]+((\.|\_|\-)[a-zA-Z0-9]+)*"
host_expression = r"([a-zA-Z]+(-[a-zA-Z]+)*)(\.[a-zA-z]+(-[a-zA-Z]+)*)+"

expression = rf"{username_expression}@{host_expression}"

matches = re.finditer(expression, text)

for match in matches:
    print(match.group())
