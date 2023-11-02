input_word = input()

reversed_word = ""

for letters in range(len(input_word) - 1, -1, -1):
    reversed_word += input_word[letters]

print(reversed_word)
