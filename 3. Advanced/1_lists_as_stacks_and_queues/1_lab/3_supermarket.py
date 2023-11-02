from collections import deque

command = input()

customers = deque()

while command != "End":
    customers.append(command)

    if command == "Paid":
        while customers:
            print(customers.popleft())

    command = input()

print(f"{len(command)} people remaining.")
