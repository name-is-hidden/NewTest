input_words = input().split()
palindrome_word = input()

palindromes_list = list()
word_counter = 0

for word in input_words:
    if word == palindrome_word:
        word_counter += 1

    if word[0] == word[-1]:
        palindromes_list.append(word)

print(palindromes_list)
print(f"Found palindrome {word_counter} times")

##################################################################################################

# input_words = input().split()
# palindrome_word = input()
#
# palindromes_list = list()
#
# for word in input_words:
#
#     reversed_list = reversed(word)
#     rev_word = "".join(reversed_list)
#     if rev_word == word:
#         palindromes_list.append(word)
#
# print(palindromes_list)
#
# word_counter = palindromes_list.count(palindrome_word)
#
# print(f"Found palindrome {word_counter} times")
#
