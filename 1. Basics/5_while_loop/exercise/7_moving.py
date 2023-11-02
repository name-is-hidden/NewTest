l = int(input())
w = int(input())
h = int(input())

volume = l * w * h

while True:
    boxes = input()

    if boxes == "Done":
        print(f"{volume} Cubic meters left.")
        break

    volume -= int(boxes)

    if volume <= 0:
        print(f"No more free space! You need {abs(volume)} Cubic meters more.")
        break
