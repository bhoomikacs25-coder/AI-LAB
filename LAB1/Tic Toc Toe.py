def win(b, p):
    return (
        any(all(x == p for x in r) for r in b) or
        any(all(b[r][c] == p for r in range(3)) for c in range(3)) or
        all(b[i][i] == p for i in range(3)) or
        all(b[i][2-i] == p for i in range(3))
    )


def bot_move(b):
    # Win or block
    for p in ["O", "X"]:
        for i in range(9):
            if b[i // 3][i % 3] == " ":
                r, c = divmod(i, 3)
                b[r][c] = p
                if win(b, p):
                    b[r][c] = " "
                    return r, c
                b[r][c] = " "

    # Center
    if b[1][1] == " ":
        return 1, 1

    # Corner
    for i in [0, 2, 6, 8]:
        r, c = divmod(i, 3)
        if b[r][c] == " ":
            return r, c

    # Any empty cell
    for i in range(9):
        r, c = divmod(i, 3)
        if b[r][c] == " ":
            return r, c


def human_move(b):
    while True:
        try:
            n = int(input("Choose 1-9: ")) - 1
            r, c = divmod(n, 3)
            if 0 <= n < 9 and b[r][c] == " ":
                return r, c
        except:
            pass
        print("Invalid move.")


def play_game(x, o):
    b = [[" "] * 3 for _ in range(3)]
    players = {"X": x, "O": o}

    for turn in range(9):
        p = "X" if turn % 2 == 0 else "O"
        r, c = players[p](b)
        b[r][c] = p

        for row in b:
            print("|".join(row))
        print()

        if win(b, p):
            print(p, "wins!")
            return

    print("Draw!")


# Choose game
choice = input("1. Bot vs Human\n2. Bot vs Bot\nChoose: ")

if choice == "1":
    play_game(human_move, bot_move)
else:
    play_game(bot_move, bot_move)