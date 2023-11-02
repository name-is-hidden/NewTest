input_text = input()
vowels_sum = 0

for letters in input_text:

    if letters == "a":
        vowels_sum += 1

    elif letters == "e":
        vowels_sum += 2

    elif letters == "i":
        vowels_sum += 3

    elif letters == "o":
        vowels_sum += 4

    elif letters == "u":
        vowels_sum += 5

print(vowels_sum)
