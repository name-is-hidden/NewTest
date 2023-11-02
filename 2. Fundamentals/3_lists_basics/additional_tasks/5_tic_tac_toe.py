first_line = input().split()
second_line = input().split()
third_line = input().split()

combined_list = first_line + second_line + third_line

axes = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]

first_player_won = any(combined_list[a] + combined_list[b] + combined_list[c] in ["111"] for a, b, c in axes)
second_player_won = any(combined_list[a] + combined_list[b] + combined_list[c] in ["222"] for a, b, c in axes)

if first_player_won:
    print("First player won")

elif second_player_won:
    print("Second player won")

else:
    print("Draw!")
