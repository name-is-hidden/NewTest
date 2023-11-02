# Write a program that prints the time 15 minutes after the input time.

hour = int(input())
minutes = int(input()) + 15

if minutes >= 60:
    hour += 1
    minutes %= 60

if hour == 24:
    hour = 0

if minutes < 10:
    print(f"{hour}:0{minutes}")

else:
    print(f"{hour}:{minutes}")
