from collections import deque

kids_string = deque(input().split())
toss = int(input())

counter = 0

while len(kids_string) > 1:
    counter += 1

    kid = kids_string.popleft()

    if counter < toss:
        kids_string.append(kid)

    else:
        print(f"Removed {kid}")
        counter = 0

print(f"Last is {kids_string.popleft()}")
