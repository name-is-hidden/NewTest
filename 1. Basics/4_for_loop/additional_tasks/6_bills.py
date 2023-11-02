months_range = int(input())

electricity_bill = 0
water_bill = 20 * months_range  # 20 per month
ethernet_bill = 15 * months_range  # 15 per month
other_bills = 0  # this equals the sum of monthly electricity, water and ethernet bills, increased by 20%
total_bills = 0

for month in range(months_range):
    current_electricity = float(input())

    electricity_bill += current_electricity
    other_bills += (current_electricity + 20 + 15) * 1.2

total_bills += electricity_bill + water_bill + ethernet_bill + other_bills

print(f'Electricity: {electricity_bill:.2f} lv')
print(f'Water: {water_bill:.2f} lv')
print(f'Internet: {ethernet_bill:.2f} lv')
print(f'Other: {other_bills:.2f}')
print(f'Average: {(total_bills / months_range):.2f} lv')
