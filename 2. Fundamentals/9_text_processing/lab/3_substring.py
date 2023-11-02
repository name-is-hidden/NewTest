text = input()
filtered_text = input()

while text in filtered_text:
    filtered_text = filtered_text.replace(text, "")


print(filtered_text)
