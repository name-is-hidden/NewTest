usernames = input().split(", ")

valid_usernames = list()

for name in usernames:
    if 3 < len(name) <= 16:
        if name.isalpha() or name.isalnum() or "-" in name or "_" in name:
            valid_usernames.append(name)

for name in valid_usernames:
    print(name)
