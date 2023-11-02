def input_characters(char_1, char_2):
    for character in range(ord(char_1) + 1, ord(char_2)):
        print(chr(character), end=" ")


first_character = input()
second_character = input()

input_characters(first_character, second_character)


################################################################################################################

# def input_characters(char_1, char_2):
#     result = list()
#     for character in range(ord(char_1) + 1, ord(char_2)):
#         result.append(chr(character))
#
#     return " ".join(result)
#
#
# first_character = input()
# second_character = input()
#
# print(input_characters(first_character, second_character))
