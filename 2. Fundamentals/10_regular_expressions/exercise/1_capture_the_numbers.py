import re

expression = r"\d+"

while True:
    text = input()
    
    if not text:
        break

    matches = re.findall(expression, text)

    if len(matches) > 0:
        print(" ".join(matches), end=" ")
