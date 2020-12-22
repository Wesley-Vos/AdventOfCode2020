def change_decks(deck_win, deck_lose):
    deck_win.extend([deck_win[0], deck_lose[0]])
    deck_win.pop(0)
    deck_lose.pop(0)

    return deck_win, deck_lose

def calc_score(deck1, deck2):
    deck = deck1 if len(deck2) == 0 else deck2
    return sum([card*(len(deck) - i) for i, card in enumerate(deck)])

def play_combat(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        if deck1[0] > deck2[0]:
            deck1, deck2 = change_decks(deck1, deck2)
        else:
            deck2, deck1 = change_decks(deck2, deck1)

    return deck1, deck2

def play_recursive_combat(deck1, deck2, sub=False):
    mem_deck1 = []
    mem_deck2 = []

    while len(deck1) > 0 and len(deck2) > 0:
        if deck1 in mem_deck1 or deck2 in mem_deck2:
            return 1
        mem_deck1.append(deck1.copy())
        mem_deck2.append(deck2.copy())
         
        if len(deck1)-1 >= deck1[0] and len(deck2)-1 >= deck2[0]:
            winner = play_recursive_combat(deck1[1:(deck1[0] + 1)],
                          deck2[1:(deck2[0] + 1)], sub=True)
        else:
            winner = 1 if deck1[0] > deck2[0] else 2

        if winner == 1:
            deck1, deck2 = change_decks(deck1, deck2)
        else:
            deck2, deck1 = change_decks(deck2, deck1)


    if sub:
        return 1 if len(deck2) == 0 else 2
    else:
        return deck1, deck2


def main():
    with open("input.txt") as f:
        raw = f.read().split("\n\n")

    deck1 = list(map(int, raw[0].splitlines()[1:]))
    deck2 = list(map(int, raw[1].splitlines()[1:]))

    print("Part 1:", calc_score(*play_combat(deck1.copy(), deck2.copy())))
    print("Part 2:", calc_score(*play_recursive_combat(deck1.copy(), deck2.copy())))


if __name__ == "__main__":
    main()
