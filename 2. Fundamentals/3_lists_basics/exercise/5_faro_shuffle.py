card_deck = input().split()
shuffle_count = int(input())

final_deck = card_deck
deck_length = int(len(card_deck) / 2)

for _ in range(shuffle_count):
    final_deck = list()
    deck_first_half = card_deck[:deck_length]
    deck_second_half = card_deck[deck_length:]

    for index in range(len(deck_first_half)):
        final_deck.append(deck_first_half[index])
        final_deck.append(deck_second_half[index])

    # if len(deck_first_half) != len(deck_first_half):       # if card deck is odd number
    #     final_deck.append(deck_second_half[-1])

    card_deck = final_deck

print(final_deck)
