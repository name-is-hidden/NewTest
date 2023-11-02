import math

magnolia_price = 3.25
hyacinth_price = 4.00
rose_price = 3.50
cactus_price = 8.00

magnolias_amount = int(input())
hyacinth_amount = int(input())
roses_amount = int(input())
cactuses_amount = int(input())
present_price = float(input())

magnolias_total = magnolia_price * magnolias_amount

hyacinth_total = hyacinth_price * hyacinth_amount

roses_total = rose_price * roses_amount

cactuses_total = cactus_price * cactuses_amount

flowers_total = magnolias_total + hyacinth_total + roses_total + cactuses_total

net_sum = flowers_total - (flowers_total * 0.05)  # 5% from the total amount is the VAT

if net_sum >= present_price:
    money_left = math.floor(net_sum - present_price)
    print(f"She is left with {money_left} leva.")

else:
    money_needed = math.ceil(present_price - net_sum)
    print(f"She will have to borrow {money_needed}")
