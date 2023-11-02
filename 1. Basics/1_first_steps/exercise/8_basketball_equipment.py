# Write a program that calculates the expense for basketball equipment:

annual_tax = int(input())

kicks_price = annual_tax - (annual_tax * 0.4)           # 40% of the annual price

jersey_price = kicks_price - (kicks_price * 0.2)        # 20% of the kicks price

ball_price = jersey_price * 0.25                        # 25% of the jersey price

accessories_price = ball_price * 0.2                    # 20% of the ball price

total_expenses = annual_tax + kicks_price + jersey_price + ball_price + accessories_price

print(total_expenses)
