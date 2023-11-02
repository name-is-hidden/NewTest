budget = float(input())
flour_price = float(input())            # Price is for 1 kilogram or 1000 grams

# The recipe for 1 bread is:
# 1 pack of eggs
# 1 kilogram of flour
# 250ml (0.250l) of milk

bread = 0
eggs = 0

eggs_price = 0.75 * flour_price         # Pack of eggs costs 75% of the 1 kilogram flour pack
milk = (flour_price * 1.25) / 4   # 1 litre of milk is 25% more expensive than 1 kilogram flour pack, and we need 250ml only.
total = flour_price + eggs_price + milk

# For every bread that you make, you will receive 3 colored eggs
# For every 3rd bread you make, you will lose some of your colored eggs after receiving
# the usual 3 colored eggs for your bread. The count of eggs you will lose is calculated
# when you subtract 2 from your current count of loaves – ({bread} – 2)

while budget >= 0:
    if budget - total > 0:
        budget -= total
        bread += 1
        eggs += 3

        if bread % 3 == 0:
            eggs -= bread - 2

    else:
        break

print(f"You made {bread} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")
