text = input()

encrypted_text = list()

for character in text:
    encrypted_text.append(ord(character))

for i in encrypted_text:
    i += 3
    print(chr(i), end="")
