expression = input()

opening_brackets = list()
pairs_brackets = {
    "{": "}",
    "[": "]",
    "(": ")"
}

balanced = True

for character in expression:
    if character in "{[(":
        opening_brackets.append(character)

    elif not opening_brackets:
        balanced = False

    else:
        last_opening_bracket = opening_brackets.pop()

        if pairs_brackets[last_opening_bracket] != character:
            balanced = False

    if not balanced:
        break

if not balanced or opening_brackets:
    print("NO")

else:
    print("YES")
