character_start = int(input())
character_end = int(input())

for characters in range(character_start, character_end + 1):
    print(f"{chr(characters)}", end=" ")
