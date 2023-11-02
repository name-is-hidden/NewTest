# Write a program that calculates if a person will have enough time to watch an episode of his favorite TV series
# during his lunch break:

import math

series = input()
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration * 0.125     # lunch_time is 1/8 of break_duration

relax_time = break_duration * 0.25      # relax_time is 1/4 of break_duration

lunch_relax = lunch_time + relax_time

free_time = break_duration - lunch_relax

if episode_duration <= free_time:
    time_left = math.ceil(free_time - episode_duration)
    print(f"You have enough time to watch {series} and left with {time_left} minutes free time.")

else:
    time_needed = math.ceil(episode_duration - free_time)
    print(f"You don't have enough time to watch {series}, you need {time_needed} more minutes.")
