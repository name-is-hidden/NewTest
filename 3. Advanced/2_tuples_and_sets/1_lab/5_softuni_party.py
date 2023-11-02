def is_vip(reservation_type):
    return reservation_type[0].isdigit()


reservations_count = int(input())

vip_reservations = set()
regular_reservations = set()

for _ in range(reservations_count):
    current_reservation = input()

    if is_vip(current_reservation):
        vip_reservations.add(current_reservation)

    else:
        regular_reservations.add(current_reservation)

while True:
    guest = input()
    if guest == "END":
        break

    elif guest in vip_reservations:
        vip_reservations.remove(guest)

    elif guest in regular_reservations:
        regular_reservations.remove(guest)

print(len(vip_reservations) + len(regular_reservations))
[print(guest) for guest in sorted(vip_reservations)]
[print(guest) for guest in sorted(regular_reservations)]
