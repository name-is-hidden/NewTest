text = input()

clear_text = ""
last_char = ""

for char in text:
    if char != last_char:
        clear_text += char
        last_char = char

print(clear_text)
