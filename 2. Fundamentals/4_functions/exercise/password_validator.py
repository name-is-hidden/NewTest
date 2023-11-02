def password_validator(password):
    length_is_valid = False
    characters_are_valid = False
    digits_are_valid = False

    if 6 <= len(password) <= 10:
        length_is_valid = True

    else:
        print("Password must be between 6 and 10 characters")

    if password.isalnum():
        characters_are_valid = True

    else:
        print("Password must consist only of letters and digits")

    digits_count = 0

    for character in password:

        if character.isdigit():
            digits_count += 1

            if digits_count >= 2:
                digits_are_valid = True
                break

    if not digits_are_valid:
        print("Password must have at least 2 digits")

    if length_is_valid and characters_are_valid and digits_are_valid:
        print("Password is valid")


input_password = input()

password_validator(input_password)
