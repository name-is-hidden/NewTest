words_count = int(input())

dict_synonyms = dict()

for item in range(words_count):
    word = input()
    synonym = input()

    if word not in dict_synonyms:
        dict_synonyms[word] = list()

    dict_synonyms[word].append(synonym)

for word, synonym in dict_synonyms.items():
    print(f"{word} - {', '.join(synonym)}")
