# payment methods take turns, starting with paying in cash and then with card
# if a products' price is above 100lv. it cannot be paid in cash
# if a products' price is below 10lv. it cannot be paid with card

money_needed = int(input())

funds_are_raised = False

counter = 0                     # counter for the transactions

cash_money = 0
cash_counter = 0

card_money = 0
card_counter = 0

command = input()

while command != "End":
    item_price = int(command)

    counter += 1

    if counter % 2 == 0 and item_price > 10:        # these are the cases for card payments

        card_money += item_price
        card_counter += 1
        print("Product sold!")

    elif counter % 2 != 0 and item_price < 100:                       # these are the cases for cash payments

        cash_money += item_price
        cash_counter += 1
        print("Product sold!")

    else:
        print("Error in transaction!")

    if cash_money + card_money >= money_needed:
        funds_are_raised = True
        break

    command = input()

average_cash = cash_money / cash_counter
average_card = card_money / card_counter

funds_raised = cash_money + card_money

if funds_are_raised:
    print(f"Average CS: {average_cash:.2f}")
    print(f"Average CC: {average_card:.2f}")

else:
    print("Failed to collect required money for charity.")
