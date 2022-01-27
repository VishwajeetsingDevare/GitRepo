board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
end = False
win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


def draw_board():
    print(board[0], board[1], board[2])
    print(board[3], board[4], board[5])
    print(board[6], board[7], board[8])


def player1():
    num = choose_number()
    if board[num] == "X" or board[num] == "O":
        print("already chosen")
        player1()
    else:
        board[num] = "X"


def player2():
    num = choose_number()
    if board[num] == "X" or board[num] == "O":
        print("already chosen")
        player2()
    else:
        board[num] = "O"


def choose_number():
    while True:
        while True:
            a = input()
            try:
                a = int(a)
                a = a - 1
                if a in range(0, 9):
                    return a
                else:
                    print("not on board")
                    continue
            except ValueError:
                print("not a number")
                continue


def check_win():
    count = 0
    for a in win_combinations:
        if board[a[0]] == board[a[1]] == board[a[2]] == "X":
            print("Player 1 won")
            return True
        if board[a[0]] == board[a[1]] == board[a[2]] == "O":
            print("Player 2 won")
            return True
    for a in range(9):
        if board[a] == "X" or board[a] == "O":
            count += 1
        if count == 9:
            print("The game ends in a Tie\n")
            return True


while not end:
    draw_board()
    end = check_win()
    if end == True:
        break
    print("Player 1 choose a place")
    player1()

    draw_board()
    end = check_win()
    if end == True:
        break
    print("Player 2 choose a place")
    player2()




