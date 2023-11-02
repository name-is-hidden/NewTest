# Write a program that calculates the renovation expenses:

nylon = 1.50            # per sq.m.
paint = 14.50           # per liter
diluent = 5.00          # per liter
bag = 0.40              # for one piece

nylon_extra = 2         # sq.m.
paint_extra = 10/100    # 10% of the total quantity

nylon_quantity = int(input()) + nylon_extra
paint_quantity = int(input())
diluent_quantity = int(input())
working_hours = int(input())

nylon_price = (nylon * nylon_quantity)

paint_price = ((paint * paint_quantity) * paint_extra) + (paint * paint_quantity)

diluent_price = diluent * diluent_quantity

materials_total = nylon_price + paint_price + diluent_price + bag

hourly_wage = materials_total * 0.3             # The hourly wage is 30% of the materials total cost

total_wage = working_hours * hourly_wage

total = total_wage + materials_total


print(total)
