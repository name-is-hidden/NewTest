# Write a program that calculates the end sum for a deposit period at a certain interest rate:

deposit = float(input())
deposit_period = int(input())
annual_interest = float(input())

annual_interest_amount = annual_interest * (deposit / 100)          # Calculate the annual interest amount

monthly_interest_amount = annual_interest_amount / 12               # Calculate the monthly interest amount

total = deposit + (deposit_period * monthly_interest_amount)        # Calculate the deposit after the period

print(total)
