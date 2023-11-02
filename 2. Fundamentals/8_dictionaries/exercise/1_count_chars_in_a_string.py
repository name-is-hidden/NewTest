text = input()

char_occurrences = dict()

for char in text:

    if char not in char_occurrences:
        char_occurrences[char] = 0

    char_occurrences[char] += 1

    if ' ' in char_occurrences.keys():
        del char_occurrences[' ']

for key, value in char_occurrences.items():
    print(f'{key} -> {value}')

#######################################################################################################################
# from collections import Counter
#
# text = input()
#
# result = Counter(text)
#
# for key, value in result.items():
#     if key != ' ':
#         print(f'{key} -> {value}')
#
# print(result)