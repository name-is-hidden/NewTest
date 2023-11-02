# Write a program that based on data can decide whether you can beat the current swimming record or not:

import math

record = float(input())
distance = float(input())
time = float(input())

resistance = math.ceil(distance // 15)     # resistance is increasing every 15 meters swum

bonus_time = resistance * 12.5             # this is the bonus time after the resistance increase

total = (distance * time) + bonus_time

if total <= record:
    print(f"Yes, he succeeded! The new world record is {total:.2f} seconds.")

else:
    needed = total - record
    print(f"No, he failed! He was {needed:.2f} seconds slower.")
