# prices depend on the competitors and on the terrain:
# for juniors terrain: trail - 5.50
# for juniors terrain: cross - country - 8
# for juniors terrain: downhill - 12.25
# for juniors terrain: road - 20

# for seniors terrain: trail - 7
# for seniors terrain: cross - country - 9.50
# for seniors terrain: downhill - 13.75
# for seniors terrain: road - 21.50

# 5% of the raised sum is taken for expenses
# There is a 25% discount if cross-country competitors are 50 or more

junior_contestants = int(input())
senior_contestants = int(input())
terrain_type = input()

juniors_fee = 0
seniors_fee = 0
discount = False                # 25%
expenses_cost = 0.05            # 5%

if terrain_type == "trail":
    juniors_fee = 5.5
    seniors_fee = 7

elif terrain_type == "cross-country":
    juniors_fee = 8
    seniors_fee = 9.5

    if junior_contestants + senior_contestants >= 50:
        discount = True

elif terrain_type == "downhill":
    juniors_fee = 12.25
    seniors_fee = 13.75

elif terrain_type == "road":
    juniors_fee = 20
    seniors_fee = 21.5

total_earnings = (juniors_fee * junior_contestants) + (seniors_fee * senior_contestants)

if discount:
    total_earnings -= total_earnings * 0.25                   # 25%

final_cost = total_earnings - (total_earnings * 0.05)

print(f"{final_cost:.2f}")
