command = input()

coffees = 0

you_need_a_rest = False

while command != "END":
    if command == "coding" or command == "dog" or command == "cat" or command == "movie":
        coffees += 1

    elif command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
        coffees += 2

    if coffees >= 5:
        you_need_a_rest = True
        break

    command = input()

if you_need_a_rest:
    print("You need extra sleep")

else:
    print(coffees)
