import sys

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

def check1():
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            board_state()
            sys.exit(f"player {board[i][0]} wins")

def check2():
    for i in range(len(board[0])):
        if board[0][i] == board[1][i] and board[1][i] == board[2][i]:
            board_state()
            sys.exit(f"player {board[0][i]} wins")

def check3():
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        board_state()
        sys.exit(f"player {board[0][0]} wins")
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        board_state()
        sys.exit(f"player {board[0][2]} wins")  

def all_checks():
    check1()
    check2()
    check3()

# and board[i][c] != 'X' and board[i][c] != 'O'

taken = []

while True:
    XTurn = ''
    OTurn = ''
    board_state()
    if type(XTurn) == int:
        XTurn = ''
    else:
        while type(XTurn) != int and XTurn not in taken:
            XTurn = int(input("Which square would you like to pick for X?- "))
            if XTurn != int and XTurn in taken:
                print('please enter a number 1-9')
                XTurn = int(input("Which square would you like to pick for X?- "))
    for i in range(len(board)):
        for c in range(len(board[i])):
            if XTurn == board[i][c]:
                board[i][c] = 'X'
                taken.append(XTurn)
                all_checks()
            else:
                pass

    board_state()

    if type(OTurn) == int:
        pass
    else:
        while type(OTurn) != int and OTurn not in taken:
            OTurn = int(input("Which square would you like to pick for O?- "))
            if OTurn != int and OTurn in taken:
                print('please enter a number 1-9')
                OTurn = int(input("Which square would you like to pick for X?- "))
    for i in range(len(board)):
        for c in range(len(board[i])):
            if OTurn == board[i][c]:
                taken.append(OTurn)
                board[i][c] = '0'
                all_checks()
            else:
                pass
    board_state()