text = input().lower().split()

occurrences_dict = dict()

for word in text:
    if word not in occurrences_dict:
        occurrences_dict[word] = 0

    occurrences_dict[word] += 1

for key, value in occurrences_dict.items():
    if value % 2 != 0:
        print(key, end=" ")

#######################################################################################################################

# input_words = input().lower().split()
#
# word_dict = dict()
#
# for word in input_words:
#     if word not in word_dict:
#         word_dict[word] = 1
#
#     else:
#         word_dict[word] += 1
#
# odd_occurrences = list()
#
# for word in word_dict.keys():
#     if word_dict[word] % 2 != 0:
#         odd_occurrences.append(word)
#
# print(" ".join(odd_occurrences))
