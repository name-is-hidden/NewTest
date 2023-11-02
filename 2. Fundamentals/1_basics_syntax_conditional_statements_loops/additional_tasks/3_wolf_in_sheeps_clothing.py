sheep_queue = input().split(", ")

if "wolf" in sheep_queue:

    if sheep_queue[-1] == "wolf":
        print("Please go away and stop eating my sheep")

    else:
        danger = len(sheep_queue) - sheep_queue.index("wolf") - 1           # -1 because the lists starts from 0 index
        print(f"Oi! Sheep number {danger}! You are about to be eaten by a wolf!")
