character_lines = int(input())

line_sum = 0

for _ in range(character_lines):
    line_sum += ord(input())

print(f"The sum equals: {line_sum}")
