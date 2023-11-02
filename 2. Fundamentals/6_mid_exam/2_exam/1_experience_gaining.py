needed_experience = float(input())
battles_count = int(input())

current_experience = 0
experience_is_enough = False

for battle in range(1, battles_count + 1):
    battle_experience = float(input())

    if battle % 3 == 0:
        battle_experience += battle_experience * 0.15

    if battle % 5 == 0:
        battle_experience -= battle_experience * 0.1

    if battle % 15 == 0:
        battle_experience += battle_experience * 0.05

    current_experience += battle_experience

    if current_experience >= needed_experience:
        experience_is_enough = True

    if experience_is_enough:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        break

if not experience_is_enough:
    print(f"Player was not able to collect the needed experience, {(needed_experience - current_experience):.2f} more needed.")
