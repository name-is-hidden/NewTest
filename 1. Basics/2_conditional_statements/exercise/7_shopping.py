# Write a program that checks whether a person can buy hardware pieces, based on the following criteria:

budget = float(input())
gpus_amount = int(input())
cpus_amount = int(input())
rams_amount = int(input())
discount = 0                    # if the gpus_amount is higher than cpus_amount there is 15% discount

gpu = 250
gpu_total = gpu * gpus_amount

cpu = gpu_total * 0.35          # 35% of the total gpus price
cpu_total = cpu * cpus_amount

ram = gpu_total * 0.1           # 10% of the total gpus price
ram_total = ram * rams_amount

total_price = gpu_total + cpu_total + ram_total

if gpus_amount > cpus_amount:
    discount = 0.15

total_price -= total_price * 0.15

if budget >= total_price:
    left = budget - total_price
    print(f"You have {left:.2f} leva left!")

else:
    required = total_price - budget
    print(f"Not enough money! You need {required:.2f} leva more!")
