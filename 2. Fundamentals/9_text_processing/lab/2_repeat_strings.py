text = input().split()

new_text = ""

for word in text:

    new_text += word * len(word)

print(new_text)
