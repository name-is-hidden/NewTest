# Calculate the price a student has to pay at the beginning of the school year:

pens = 5.80
markers = 7.20
cleaner = 1.20

pens_amount = int(input())
markers_count = int(input())
cleaner_amount = int(input())
discount = int(input())             # This is discounted from the total price

pens_price = pens * pens_amount

markers_price = markers * markers_count

cleaner_price = cleaner * cleaner_amount

total = pens_price + markers_price + cleaner_price

discount_amount = total * (discount / 100)

final_price = total - discount_amount

print(final_price)
