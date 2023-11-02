# prices depend on the group - gender and the vacation season:
# during winter:
# boys/girls - 9.60, mixed group - 10

# during spring:
# boys/girls - 7.20, mixed group - 9.50

# during summer:
# boys/girls - 15, mixed group - 20

season = input()
group = input()
students = int(input())
nights = int(input())

price = 0
sport = " "

# sports are fixed for different groups during different seasons:

# during winter:
# girls do gymnastics, boys do judo, mixed groups do ski

# during spring:
# girls do athletics, boys play tennis, mixed groups go cycling

# during summer:
# girls play volleyball, boys play football, mixed groups go swimming

if season == "Winter":

    if group == "boys":
        sport = "Judo"
        price = 9.60

    elif group == "girls":
        sport = "Gymnastics"
        price = 9.60

    else:
        sport = "Ski"
        price = 10.00


elif season == "Spring":

    if group == "boys":
        sport = "Tennis"
        price = 7.20

    elif group == "girls":
        sport = "Athletics"
        price = 7.20

    else:
        sport = "Cycling"
        price = 9.50


elif season == "Summer":
    if group == "boys":
        sport = "Football"
        price = 15

    elif group == "girls":
        sport = "Volleyball"
        price = 15

    else:
        sport = "Swimming"
        price = 20

total = price * students * nights

if students >= 50:          # 50% discount if there are 50 or more students
    total -= total * 0.5

elif 20 <= students < 50:   # 15 % discount if there are 20 or more but less than 50 students
    total -= total * 0.15

elif 10 <= students < 20:   # 5% discount if there are 10 or more but less than 20 students
    total -= total * 0.05

print(f"{sport} {total:.2f} lv.")
