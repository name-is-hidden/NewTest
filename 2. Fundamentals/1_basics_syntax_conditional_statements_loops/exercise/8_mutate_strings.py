first_string = input()
second_string = input()

new_word = ''

for char in range(len(first_string)):
    new_string = second_string[:char] + first_string[char:len(first_string)]

    if new_string not in (first_string, second_string, new_word):
        print(new_string)
        new_word = new_string

print(second_string)
