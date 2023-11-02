days_off = int(input())
year = 365
annual_play = 30000                     # the annual playtime rate

workdays = year - days_off

workdays_play = workdays * 63           # the playtime during workdays

days_off_play = days_off * 127          # the playtime during days off

total_play = workdays_play + days_off_play

overplay = total_play - annual_play

underplay = annual_play - total_play


if annual_play <= total_play:
    hours = overplay // 60
    minutes = overplay % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

else:
    hours = underplay // 60
    minutes = underplay % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
