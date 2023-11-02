def office_management(rooms_count):
    free_chairs = 0
    special_condition = True

    for room in range(1, rooms_count + 1):
        room_data = input().split()
        available_chairs = room_data[0]
        visitors_count = int(room_data[1])

        difference = len(available_chairs) - visitors_count

        if difference >= 0:
            free_chairs += difference

        else:
            special_condition = False
            print(f"{abs(difference)} more chairs needed in room {room}")

    if special_condition:
        print(f"Game On, {free_chairs} free chairs left")


number_of_rooms = int(input())
office_management(number_of_rooms)
