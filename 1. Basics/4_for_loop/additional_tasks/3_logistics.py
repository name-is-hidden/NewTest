cargo_count = int(input())

total_weight = 0
cargo_price = 0
total_cargo_price = 0

bus_cargo = 0
truck_cargo = 0
train_cargo = 0

for cargo in range(cargo_count):
    cargo_weight = int(input())
    total_weight += cargo_weight

    if cargo_weight <= 3:           # 3 tons or fewer are to be driven by bus
        cargo_price = 200
        bus_cargo += cargo_weight

    elif 4 <= cargo_weight <= 11:    # between 4 and 11 tons are to be driven by truck
        cargo_price = 175
        truck_cargo += cargo_weight

    elif cargo_weight >= 12:        # 12 tons or more are to be driven by train
        cargo_price = 120
        train_cargo += cargo_weight

    total_cargo_price += cargo_weight * cargo_price

average_cargo_price = total_cargo_price / total_weight

bus_percentage = (bus_cargo / total_weight) * 100
truck_percentage = (truck_cargo / total_weight) * 100
train_percentage = (train_cargo / total_weight) * 100

print(f"{average_cargo_price:.2f}")
print(f"{bus_percentage:.2f}%")
print(f"{truck_percentage:.2f}%")
print(f"{train_percentage:.2f}%")
