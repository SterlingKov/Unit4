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



"""def check1():
    for i in range(len(board)):
        if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
            print(f"player {board[i][0]} wins")
            break

def check2():
    for i in range(len(board[0])):
        if board[0][i] == board[0][i+1] and board[0][i+1] == board[0][i+2]:
            print(f"player {board[0][i]} wins")
            break

def check3():
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        print(f"player {board[0][0]} wins")
    elif board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        print(f"player {board[0][2]} wins")"""

# and board[i][c] != 'X' and board[i][c] != 'O'

taken = []

while True:
    t = False
    f = True
    print(t)
    XTurn = ''
    OTurn = ''
    board_state()
    if type(XTurn) == int:
        XTurn = ''
    else:
        while type(XTurn) != int and XTurn not in taken:
            XTurn = int(input("Which square would you like to pick for X?- "))
    for i in range(0, len(board)-1):
        for c in range(0, len(board[i])-1):
            print(XTurn)
            print(board[i][c])
            if XTurn == board[i][c] and board[i][c] != 'X' and board[i][c] != 'O':
                print(XTurn)
                board[i][c] = 'X'
                taken.append(XTurn)
                t = True
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
            elif t:
                print("yes")
                break
            else:
                print("this square is already taken")
                f = False
                print(1)
                break
        if f:
            print(6)
            pass
        else:
            print(3)
            break
    if f:
        print(4)
        pass
    else:
        print(5)
        continue


    board_state()

    if type(OTurn) == int:
        pass
    else:
        while type(OTurn) != int:
            OTurn = int(input("Which square would you like to pick for O?- "))
    for i in range(len(board)):
        for c in range(len(board[i])):
            if OTurn == board[i][c] and board[i][c] not in taken:
                taken.append(board[i][c])
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

    