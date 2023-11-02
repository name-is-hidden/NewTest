from collections import deque

stations_amount = int(input())

amount_and_range = deque()

for _ in range(stations_amount):
    amount_and_range.append([int(x) for x in input().split()])

for attempt in range(stations_amount):
    trunk = 0
    failed = False

    for petrol, distance in amount_and_range:
        trunk += petrol - distance

        if trunk < 0:
            failed = True
            break

    if failed:
        amount_and_range.append(amount_and_range.popleft())

    else:
        print(attempt)
        break
