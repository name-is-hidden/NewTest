exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())


exam_time = exam_hour * 60 + exam_minute            # turn it into minutes

arrival_time = arrival_hour * 60 + arrival_minute   # this as well

on_time_result = exam_time - arrival_time

late_result = arrival_time - exam_time

if late_result > 0:
    print("Late")

    if arrival_time != exam_time:
        hours = late_result // 60
        minutes = late_result % 60

        if hours >= 1:
            print(f"{hours}:{minutes:02d} hours after the start")

        else:
            print(f"{minutes} minutes after the start")

elif 0 <= on_time_result <= 30:
    minutes = on_time_result % 60
    print("On time")
    print(f"{minutes} minutes before the start")

elif on_time_result > 30:
    print("Early")

    if exam_time != arrival_time:
        hours = on_time_result // 60
        minutes = on_time_result % 60

        if hours > 0:
            print(f"{hours}:{minutes:02d} hours before the start")

        else:
            print(f"{minutes} minutes before the start")
