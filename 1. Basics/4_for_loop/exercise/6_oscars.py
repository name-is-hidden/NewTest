actor_name = input()
initial_academy_points = float(input())
judges_count = int(input())

points = 0
total_points = 0


for judges in range(judges_count):
    current_judge = input()
    judge_points = float(input())
    points += judge_points * len(current_judge) / 2
    total_points = points + initial_academy_points

    if total_points > 1250.5:               # 1250.5 is the minimum amount of points to get nominated
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_points:.1f}!")
        break

if total_points <= 1250.5:
    needed = 1250.5 - total_points
    print(f"Sorry, {actor_name} you need {needed:.1f} more!")
