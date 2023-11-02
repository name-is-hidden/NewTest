food = int(input()) * 1000
command = input()


while command != "Adopted":
    food_eaten = int(command)
    food -= food_eaten
    command = input()

if food >= 0:
    print(f"Food is enough! Leftovers: {food} grams.")

else:
    print(f"Food is not enough. You need {abs(food)} grams more.")
