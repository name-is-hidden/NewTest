deposited_amount = input()
total = 0

while deposited_amount != "NoMoreMoney":
    current_deposit = float(deposited_amount)

    if current_deposit < 0:
        print(f"Invalid operation!")
        break

    total += current_deposit

    print(f"Increase: {current_deposit:.2f}")

    deposited_amount = input()

print(f"Total: {total:.2f}")
