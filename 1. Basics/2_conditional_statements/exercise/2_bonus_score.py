# Write a program that calculates a bonus to an input number and prints the bonus and the number with bonus:

a = int(input())

bonus = 0
total = 0

if a <= 100:
    bonus = 5
    total = a + bonus

elif 100 < a <= 1000:
    bonus = a * 0.2     # the bonus in this interval is 20% of the number
    total = a + bonus

else:
    bonus = a * 0.1     # the bonus in this interval is 10% of the number
    total = a + bonus

if a % 2 == 0:          # additional score if the number is even
    bonus += 1
    total = a + bonus

elif a % 10 == 5:       # additional if the number ends in 5
    bonus += 2
    total = a + bonus

print(bonus)
print(total)
