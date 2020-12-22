def change_decks(deck_win, deck_lose):
    deck_win.append(deck_win[0])
    deck_win.append(deck_lose[0])
    deck_win.pop(0)
    deck_lose.pop(0)

    return deck_win, deck_lose


def part1(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1[0] > deck2[0]:
            deck1, deck2 = change_decks(deck1, deck2)
        else:
            deck1, deck2 = change_decks(deck2, deck1)

    deck = deck1 if len(deck1) > 0 else deck2
    return sum([card*(len(deck) - i) for i, card in enumerate(deck)])


def game(deck1, deck2, sub=False):
    print("New game started")
    history_player1 = []
    history_player2 = []
    round = 1

    while len(deck1) > 0 and len(deck2) > 0:
        print("Round", round)
        print("Deck 1:", deck1)
        print("Deck 2:", deck2)

        if deck1 in history_player1 or deck2 in history_player2:
            print(history_player1 if deck1 in history_player1 else history_player2)
            print("Player 1 wins, found in history deck",
                  1 if deck1 in history_player1 else 2)

            history_player1.append(deck1)
            history_player2.append(deck2)

            deck1, deck2 = change_decks(deck1, deck2)
        else:
            history_player1.append(deck1)
            history_player2.append(deck2)

        if (len(deck1) - 1) >= deck1[0] and (len(deck2) - 1) <= deck2[0]:
            winner = game(deck1[1:(deck1[0] + 1)],
                          deck2[1:(deck2[0] + 1)], sub=True)
            if winner == 1:
                deck1, deck2 = change_decks(deck1, deck2)
            else:
                deck1, deck2 = change_decks(deck1, deck2)
            break

        else:
            if deck1[0] > deck2[0]:
                print("Player 1 wins (higer card)")
                deck1, deck2 = change_decks(deck1, deck2)
            else:
                print("Player 2 wins (higher card)")
                deck1, deck2 = change_decks(deck2, deck1)

        # history_player1.append(deck1)
        # history_player2.append(deck2)
        round += 1

    if sub:
        print("Player", 1 if len(deck2) == 0 else 2, "won the game, go back")
        return 1 if len(deck2) == 0 else 2
    else:
        deck = deck1 if len(deck1) > 0 else deck2
        return sum([card*(len(deck) - i) for i, card in enumerate(deck)])


def main():
    with open("test_input.txt") as f:
        raw = f.read().split("\n\n")

    deck1 = list(map(int, raw[0].splitlines()[1:]))
    deck2 = list(map(int, raw[1].splitlines()[1:]))

    #print("Part 1:", part1(deck1, deck2))
    print("Part 2:", game(deck1, deck2))


if __name__ == "__main__":
    main()
