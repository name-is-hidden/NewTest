import re

expression = r"^!(?P<command>[A-Z][a-z]{2,})!:\[(?P<message>[A-Za-z]{8,})\]$"
number_of_messages = int(input())

for item in range(number_of_messages):
    current_message = input()

    match = re.match(expression, current_message)

    decryption_list = []

    if match:

        for char in match.group("message"):
            decryption_list.append(str(ord(char)))

        print(f"{match.group('command')}: {' '.join(decryption_list)}")

    else:
        print("The message is invalid")



# import re
#
# strings_count = int(input())
#
# translation_list = list()
#
# for text in range(strings_count):
#     current_text = input()
#
#     expression = r"(!)([A-Z][a-z]{2,})(!):(\[)([A-Za-z]{8,})(\])"
#
#     match = re.finditer(expression, current_text)
#
#     if match is not None:
#         for item in match:
#             translation_list.append(item.group(5).split())
#
#     else:
#         print("The message is invalid")
