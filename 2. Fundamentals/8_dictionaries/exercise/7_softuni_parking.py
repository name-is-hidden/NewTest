commands_count = int(input())

registrations_dict = dict()

for i in range(commands_count):
    line = input().split()
    command, name = line[0], line[1]

    if command == "register":
        number = line[2]

        if name not in registrations_dict:
            registrations_dict[name] = number
            print(f"{name} registered {number} successfully")

        else:
            print(f"ERROR: already registered with plate number {number}")

    if command == "unregister":

        if name not in registrations_dict:
            print(f"ERROR: user {name} not found")

        else:
            print(f"{name} unregistered successfully")
            del registrations_dict[name]

for name, number in registrations_dict.items():
    print(f"{name} => {number}")
