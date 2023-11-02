text = input()

for word in range(len(text)):
    if text[word] == ":":
        print(f"{text[word]}{text[word + 1]}")
