distance = int(input())
daytime = input()

total = 0

# all prices are in BGN (lv)
# if the transport method is taxi the is no minimum range. The prices are 0.70 initial and 0.79 or 0.90 per kilometer
# depending on the daytime.
# if the transport method is by bus, the minimum range is 20km. and the price is 0.09 per kilometer.
# if the transport method is by train, the minimum range is 100km. and the price is 0.06 per kilometer

if distance < 20:
    if daytime == "day":
        total = 0.70 + (0.79 * distance)

    elif daytime == "night":
        total = 0.70 + (0.90 * distance)

elif 20 <= distance < 100:
    total = 0.09 * distance

else:
    total = 0.06 * distance

print(f"{total:.2f}")
