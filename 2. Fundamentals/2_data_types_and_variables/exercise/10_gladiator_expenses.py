losses = int(input())

# Prices:

helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

expenses = 0
broken_shield = 0

for loss in range(1, losses + 1):

    if loss % 2 == 0:
        expenses += helmet

    if loss % 3 == 0:
        expenses += sword

    if loss % 2 == 0 and loss % 3 == 0:
        expenses += shield
        broken_shield += 1

if broken_shield > 1:
    expenses += armor * (broken_shield // 2)

print(f"Gladiator expenses: {expenses:.2f} aureus")
