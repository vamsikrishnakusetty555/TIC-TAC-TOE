# TIC TAC TOE by VAMSI KRISHNA
import random
def game_board(board):
    print("\n#Board")
    x = "|".join(board[0])
    y = "|".join(board[1])
    z = "|".join(board[2])
    print("\t", x)
    print("\t", y)
    print("\t", z)
def position_check(r,c,i,board):
    if board[int(r) - 1][int(c) - 1] == "-":
        if i%2!=0:
            board[int(r) - 1][int(c) - 1] = "x"
            game_board(board)
        elif i%2==0:
            board[int(r) - 1][int(c) - 1] = "o"
            game_board(board)
    else:
        print()
        print("SORRY, ALready Occupied!"
              "Choose Another!!🦉 ")
        r, c = input("Enter (Row,Column) number to Fix the Spot: ").split(",")
        position_check(r,c,i,board)
def position_check_computer(r,c,i,board):
    if board[int(r) - 1][int(c) - 1] == "-":
        if i%2!=0:
            board[int(r) - 1][int(c) - 1] = "x"
            game_board(board)
        elif i%2==0:
            board[int(r)- 1][int(c) - 1] = "o"
            game_board(board)
    else:
        r = random.randint(1, 3)
        c = random.randint(1, 3)
        position_check_computer(r,c,i,board)
def win_check(board,i):
    if i%2!=0:
        # WINNING CONDITION FOR PLAYER X
        if board[0][0] == "x" and board[0][1] == "x" and board[0][2] == "x":
            return "X"
        elif board[1][0] == "x" and board[1][1] == "x" and board[1][2] == "x":
            return "X"
        elif board[2][0] == "x" and board[2][1] == "x" and board[2][2] == "x":
            return "X"
        elif board[0][0] == "x" and board[1][0] == "x" and board[2][0] == "x":
            return "X"
        elif board[0][1] == "x" and board[1][1] == "x" and board[2][1] == "x":
            return "X"
        elif board[0][2] == "x" and board[1][2] == "x" and board[2][2] == "x":
            return "X"
        elif board[0][0] == "x" and board[1][1] == "x" and board[2][2] == "x":
            return "X"
        elif board[0][2] == "x" and board[1][1] == "x" and board[2][0] == "x":
            return "X"
    elif i%2==0:
        # WINNING CONDITION FOR O
        if board[0][0] == "o" and board[0][1] == "o" and board[0][2] == "o":
            return "O"
        elif board[1][0] == "o" and board[1][1] == "o" and board[1][2] == "o":
            return "O"
        elif board[2][0] == "o" and board[2][1] == "o" and board[2][2] == "o":
            return "O"
        elif board[0][0] == "o" and board[1][0] == "o" and board[2][0] == "o":
            return "O"
        elif board[0][1] == "o" and board[1][1] == "o" and board[2][1] == "o":
            return "O"
        elif board[0][2] == "o" and board[1][2] == "o" and board[2][2] == "o":
            return "O"
        elif board[0][0] == "o" and board[1][1] == "o" and board[2][2] == "o":
            return "O"
        elif board[0][2] == "o" and board[1][1] == "o" and board[2][0] == "o":return "O"

#Main CODE.....
print("TIC-TAC-TOE")
print("--------------------------------------")
print('''Play as   1. Single Player
          2. Multi Player''')
choice=int(input("\nEnter Choice (1/2): "))
board = [["-" for i in range(3)] for j in range(3)]
game_board(board)
if choice==1:
    player_choice=input("\nPlay as 'X' or 'O': ")
    if player_choice.upper()=="X":
        for i in range(1, 10):
            print()
            if i % 2 != 0:
                print(">>>Player - X")
                r, c = input("Enter (Row,Column) number to Fix the Spot: ").split(",")
                position_check(r, c, i, board)
                result = win_check(board, i)
                if result == "X":
                    print("X - won")
                    break
            if i % 2 == 0:
                print(">>>Player - O (AI)")
                r=random.randint(1,3)
                c=random.randint(1,3)
                position_check_computer(r, c, i, board)
                result = win_check(board, i)
                if result == "O":
                    print("O - won (AI)")
                    break
        else:
            print("Draw!!")
    elif player_choice.upper()=="O":
        for i in range(1, 10):
            print()
            if i % 2 != 0:
                print(">>>Player - X (AI)")
                r = random.randint(1, 3)
                c = random.randint(1, 3)
                position_check_computer(r, c, i, board)
                result = win_check(board, i)
                if result == "X":
                    print("X - won (AI)")
                    break
            if i % 2 == 0:
                print(">>>Player - O")
                r, c = input("Enter (Row,Column) number to Fix the Spot: ").split(",")
                position_check(r, c, i, board)
                result = win_check(board, i)
                if result == "O":
                    print("O - won ")
                    break
        else:
            print("Draw!!")
    else:
        print("Invalid Choice!")
elif choice==2:
    for i in range(1,10):
        print()
        if i%2!=0:
            print(">>>Player - X")
            r, c = input("Enter (Row,Column) number to Fix the Spot: ").split(",")
            position_check(r,c,i,board)
            result=win_check(board,i)
            if result=="X":
                print("X - won")
                break
            print()
        if i%2==0:
            print(">>>Player - O")
            r, c = input("Enter (Row,Column) number to Fix the Spot: ").split(",")
            position_check(r,c,i,board)
            result=win_check(board,i)
            if result=="O":
                print("O - won")
                break
    else:
        print("Draw!!")
else:
    print("\nInvalid Option!")
