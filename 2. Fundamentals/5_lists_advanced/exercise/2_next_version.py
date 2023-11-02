def next_version(version_number):
    version_number = int("".join(version_number)) + 1
    result = [str(x) for x in str(version_number)]
    print(".".join(result))


current_version = input().split(".")

next_version(current_version)
