# Find how much will yard greening cost with the following data:

price = 7.61                # Price per sq.m. with TAX

yard_area = float(input())

discount = 18/100           # Discount because the yard is very big

total_price = price * yard_area

discount_amount = discount * total_price

final_price = total_price - discount_amount

print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount_amount} lv.")
