line = input()

nett_price = 0
tax = 0.2               # TAX is 20%
discount = 0.1         # Discount is 5% only applicable to special clients

while line != "special" and line != "regular":
    current_price = float(line)

    if current_price >= 0:
        nett_price += current_price

    else:
        print("Invalid price!")

    line = input()

brutt_price = nett_price + (nett_price * tax)

if brutt_price <= 0:
    print("Invalid order!")

else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {nett_price:.2f}$")
    print(f"Taxes: {(brutt_price - nett_price):.2f}$")
    print("-----------")
    if line == "special":
        brutt_price -= brutt_price * discount
    print(f"Total price: {brutt_price:.2f}$")
