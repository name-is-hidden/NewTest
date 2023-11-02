# Write a program that calculates the price of certain fish species:

mackerel = float(input())
sprat = float(input())
bonito_amount = float(input())
scad_amount = float(input())
mussels_amount = int(input())


bonito = (mackerel + (mackerel * 0.6)) * bonito_amount
scad = (sprat + (sprat * 0.8)) * scad_amount
mussels = mussels_amount * 7.50

total = bonito + scad + mussels

print(f"{total:.2f}")
