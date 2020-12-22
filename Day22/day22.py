def main():
    with open("input.txt") as f:
        raw = f.read().split("\n\n")
    
    player1 = list(map(int, raw[0].splitlines()[1:]))
    player2 = list(map(int, raw[1].splitlines()[1:]))
    
    while len(player1) > 0 and len(player2) > 0:
        if player1[0] > player2[0]:
            player1.append(player1[0])
            player1.append(player2[0])
            player1.pop(0)
            player2.pop(0)
        else:
            player2.append(player2[0])
            player2.append(player1[0])
            player2.pop(0)
            player1.pop(0)
    print(len(player1), len(player2))
    
    deck = player1 if len(player1) > 0 else player2
    sum_val = 0
    for i, card in enumerate(deck):
        sum_val += card*(len(deck) - i)
        
    print(sum_val)
    
    
    
if __name__ == "__main__":
    main()