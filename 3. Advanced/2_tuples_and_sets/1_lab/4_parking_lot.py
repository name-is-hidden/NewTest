parking_lot_log = [input().split(", ") for _ in range(int(input()))]

parked_cars = set()

for direction, car_plate in parking_lot_log:
    if direction == "IN":
        parked_cars.add(car_plate)

    elif direction == "OUT":                # could be "else:"
        parked_cars.remove(car_plate)

if parked_cars:
    [print(car) for car in parked_cars]

else:
    print("Parking Lot is Empty")
