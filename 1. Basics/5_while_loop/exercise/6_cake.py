cake_width = int(input())
cake_length = int(input())

cake = cake_length * cake_width

while True:
    pieces_taken = input()

    if pieces_taken == "STOP":
        print(f"{cake} pieces are left.")
        break

    cake -= int(pieces_taken)

    if cake <= 0:
        print(f"No more cake left! You need {abs(cake)} pieces more.")
        break
