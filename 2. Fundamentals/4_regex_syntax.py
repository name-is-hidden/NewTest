# ########## SPECIAL SEQUENCES #########

# \d - Returns a match where the string contains DIGITS (numbers from 0-9)

# \D - Returns a match where the string DOES NOT contain digits

# \b - Returns a match where the specified characters are at the BEGINNING or at the END of a word

# \s - Returns a match where the string contains a WHITE SPACE character

# \S - Returns a match where the string DOES NOT contain a white space character

# \w - Returns a match where the string contains any WORD characters (characters from "a" to "Z", digits from 0 - 9
# and the underscore character)

# \W - Returns a match where the string DOES NOT contain any word characters


# ########## METACHARACTERS ##########

# \ - Signals a special sequence and can also be used to escape special characters

# . - Any character except new line character

# + - One or more occurrences

# * - Zero or more occurrences

# | - either or

# () - capture and group

# {} - exactly the specified number of occurrences

# ^ - starts with

# $ - ends with


# ########## SETS ##########

# [arn] - Returns a match where ONE of the specified characters ("a", "r" or "n" are present)

# [a-n] - Returns a match for any LOWER - CASE character, alphabetically between "a" and "n"

# [^arn] - Returns a match for any character EXCEPT "a", "r" and "n"

# [0123] - Returns a match where ANY of the specified digits 0, 1, 2 or 3 are present

# [0-9] - Returns a match for any digit BETWEEN 0 and 9

# [0-5][0-9] - Returns a match for any two-digit numbers from 00 and 59

# [a-zA-Z] - Returns a match for any character ALPHABETICALLY between "a" and "z", lower case OR upper case
