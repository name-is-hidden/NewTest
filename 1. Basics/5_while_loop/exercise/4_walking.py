goal = 10000
total_steps = 0

while True:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        total_steps += steps

        if total_steps >= goal:
            print(f"Goal reached! Good job!")
            print(f"{total_steps - 10000} steps over the goal!")
            break

        else:
            print(f"{goal - total_steps} more steps to reach goal.")

        break

    total_steps += int(steps)

    if total_steps >= goal:
        print("Goal reached! Good job!")
        print(f"{total_steps - goal} steps over the goal!")
        break
