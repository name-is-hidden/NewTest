def palindrome(word, position):
    if position >= len(word) // 2:
        return f"{word} is a palindrome"

    left = word[position]
    right = word[-1 - position]

    if left != right:
        return f"{word} is not a palindrome"

    return palindrome(word, position + 1)
