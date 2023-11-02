import math

gpu = int(input())
adapter = int(input())
gpu_energy_consumption = float(input())
brut_profit = float(input())

gpus_total_price = 13 * gpu
adapters_total_price = 13 * adapter
total_expenses = gpus_total_price + adapters_total_price + 1000
net_profit_per_gpu = brut_profit - gpu_energy_consumption
total_profit = net_profit_per_gpu * 13

investment_return_period = total_expenses / total_profit

print(total_expenses)
print(math.ceil(investment_return_period))
