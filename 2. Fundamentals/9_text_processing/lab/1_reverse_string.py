word = input()

reversed_word = ""

while word != "end":
    reverse = reversed(word)

    reversed_word = "".join(reverse)

    print(f"{word} = {reversed_word}")

    word = input()

#######################################################################################################################

# word = input()
#
# while word != "end":
#
#     print(f"{word} = {word[::-1]}")
#
#     word = input()

#######################################################################################################################
#
# word = input()
#
# while word != "end":
#     word_reversed = ""
#
#     for char in reversed(word):
#         word_reversed += char
#
#     print(f"{word} = {word_reversed}")
#
#     word = input()

