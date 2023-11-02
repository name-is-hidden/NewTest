input_numbers = list(map(int, input().split(', ')))
boundary = 10

while len(input_numbers) > 0:
    result = [x for x in input_numbers if x <= boundary]
    print(f'Group of {boundary}\'s: {result}')
    input_numbers = [x for x in input_numbers if x not in result]
    boundary += 10
