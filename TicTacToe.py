board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def board_state():
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}")
    print( "----------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print( "----------")
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print( "----------")



while True:
    XTurn = ''
    OTurn = ''
    if type(XTurn) == int:
        pass
    else:
        while type(XTurn) != int:
            XTurn = int(input("Which square would you like to pick for X?- "))
    for i in range(len(board)):
        for c in range(len(board[i])):
            if XTurn == board[i][c]:
                board[i][c] = 'X'
                for i in range(len(board)):
                    if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                        board_state()
                        print(f"player {board[i][0]} wins")
                        quit()
                for i in range(len(board[0])):
                    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                        board_state()
                        print(f"player {board[0][i]} wins")
                        quit()
                if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                    board_state()
                    print(f"player {board[0][0]} wins")
                elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                    board_state()
                    print(f"player {board[0][2]} wins")
                    quit()
                
            else:
                
                pass

    board_state()

    if type(OTurn) == int:
        pass
    else:
        while type(OTurn) != int:
            OTurn = int(input("Which square would you like to pick for O?- "))
    for i in range(len(board)):
        for c in range(len(board[i])):
            if OTurn == board[i][c]:
                board[i][c] = '0'
                for i in range(len(board)):
                    if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                        board_state()
                        print(f"player {board[i][0]} wins")
                        quit()
                for i in range(len(board[0])):
                    if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
                        board_state()
                        print(f"player {board[0][i]} wins")
                        quit()
                if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
                    board_state()
                    print(f"player {board[0][0]} wins")
                elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
                    board_state()
                    print(f"player {board[0][2]} wins")
                    quit()
            else:
                pass
    board_state()

    