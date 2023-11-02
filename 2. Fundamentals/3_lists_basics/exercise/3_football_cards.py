kicked_players = input().split()

list_of_kicked_players = list()

team_a = 11
team_b = 11

team_is_out = False

for players in kicked_players:
    if players not in list_of_kicked_players:

        if "A" in players:
            team_a -= 1
            list_of_kicked_players.append(players)

        elif "B" in players:
            team_b -= 1
            list_of_kicked_players.append(players)

        if team_a < 7 or team_b < 7:
            team_is_out = True
            break

print(f"Team A - {team_a}; Team B - {team_b}")

if team_is_out:
    print("Game was terminated")

###########################################################################################################
#
# player_cards = input().split()
#
# team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
#
# team_is_out = False
#
# for player in player_cards:
#
#     if player in team_a:
#         team_a.remove(player)
#
#     elif player in team_b:
#         team_b.remove(player)
#
#     if len(team_a) < 7 or len(team_b) < 7:
#         team_is_out = True
#         break
#
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
#
# if team_is_out:
#     print("Game was terminated")

############################################################################################################
#
# kicked_players = input().split()
#
# team_a = 11
# team_b = 11
#
# a_kicked_list = list()
# b_kicked_list = list()
#
# game_is_terminated = False
#
# for player in kicked_players:
#     if "A" in player:
#         if player not in a_kicked_list:
#             a_kicked_list.append(player)
#
#     elif "B" in player:
#         if player not in b_kicked_list:
#             b_kicked_list.append(player)
#
# # if either team loses 4 player or more, the other automatically wins
#
#     if len(a_kicked_list) > 4:
#         game_is_terminated = True
#         break
#
#     elif len(b_kicked_list) > 4:
#         game_is_terminated = True
#         break
#
# if game_is_terminated:
#     print(f"Team A - {team_a - (len(a_kicked_list))}; Team B - {team_b - len(b_kicked_list)}")
#     print("Game was terminated")
#
# else:
#     print(f"Team A - {team_a - (len(a_kicked_list))}; Team B - {team_b - len(b_kicked_list)}")
