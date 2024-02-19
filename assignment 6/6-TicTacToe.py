import pyfiglet
import random
import time
from termcolor import colored

title = pyfiglet.figlet_format("Tic Toc Toe" , font = "slant")
print(title)

start = time.time()
######################################################################### functions
def show():
    for i in range(3):
        for j in range(3):

            if game_board[i][j] == "X":
                print(colored(game_board[i][j],"red"),end=" ")
            elif game_board[i][j] == "O":
                print(colored(game_board[i][j],"blue"),end=" ")
            else:
                print(game_board[i][j] , end=" ")
        print()

def mytime():
     end = time.time()
     total_time = end - start
     print("Time spent playing:"+ str(total_time))


def check_game():

################### Rows
    if game_board[0][0] =="X" and game_board[0][1] =="X" and game_board[0][2]=="X":
        if (p==1):
            print("Player 1 wins!!!🎉")
        else:
            print("CPU wins!!!🎉")
        mytime()
        exit()

    elif game_board[1][0] =="X" and game_board[1][1] =="X" and game_board[1][2]=="X":
        if (p==1):
            print("Player 1 wins!!!🎉")
        else:
            print("CPU wins!!!🎉")
        mytime()
        exit()

    elif game_board[2][0] =="X" and game_board[2][1] =="X" and game_board[2][2]=="X":
        if (p==1):
            print("Player 1 wins!!!🎉")
        else:
            print("CPU wins!!!🎉")
        mytime()
        exit()

    elif game_board[0][0] =="O" and game_board[0][1] =="O" and game_board[0][2]=="O":
        if (p==1):
            print("Player 2 wins!!!🎉")
        else:
            print("Player wins!!!🎉")
        mytime()
        exit()

    elif game_board[1][0] =="O" and game_board[1][1] =="O" and game_board[1][2]=="O":
        if (p==1):
            print("Player 2 wins!!!🎉")
        else:
            print("Player wins!!!🎉")
        mytime()
        exit()

    elif game_board[2][0] =="O" and game_board[2][1] =="O" and game_board[2][2]=="O":
        if (p==1):
            print("Player 2 wins!!!🎉")
        else:
            print("Player wins!!!🎉")
        mytime()
        exit()

################### cols
    if game_board[0][0] =="X" and game_board[1][0] =="X" and game_board[2][0]=="X":
        if (p==1):
            print("Player 1 wins!!!🎉")
        else:
            print("CPU wins!!!🎉")
        mytime()
        exit()

    elif game_board[0][1] =="X" and game_board[1][1] =="X" and game_board[2][1]=="X":
        if (p==1):
            print("Player 1 wins!!!🎉")
        else:
            print("CPU wins!!!🎉")
        mytime()
        exit()

    elif game_board[0][2] =="X" and game_board[1][2] =="X" and game_board[2][2]=="X":
        if (p==1):
            print("Player 1 wins!!!🎉")
        else:
            print("CPU wins!!!🎉")
        mytime()
        exit()

    elif game_board[0][0] =="O" and game_board[1][0] =="O" and game_board[2][0]=="O":
        if (p==1):
            print("Player 2 wins!!!🎉")
        else:
            print("Player wins!!!🎉")
        mytime()
        exit()

    elif game_board[0][1] =="O" and game_board[1][1] =="O" and game_board[2][1]=="O":
        if (p==1):
            print("Player 2 wins!!!🎉")
        else:
            print("Player wins!!!🎉")
        mytime()
        exit()

    elif game_board[0][2] =="O" and game_board[1][2] =="O" and game_board[2][2]=="O":
        if (p==1):
            print("Player 2 wins!!!🎉")
        else:
            print("Player wins!!!🎉")
        mytime()
        exit()

################### Diameters
    if game_board[0][0] =="X" and game_board[1][1] =="X" and game_board[2][2] == "X":
        if (p==1):
            print("Player 1 wins!!!🎉")
        else:
            print("CPU wins!!!🎉")
        mytime()
        exit()
    
    elif game_board[0][2] == "X" and game_board[1][1] =="X" and game_board[2][0] =="X":
        if (p==1):
            print("Player 1 wins!!!🎉")
        else:
            print("CPU wins!!!🎉")
        mytime()
        exit()

    if game_board[0][0] =="O" and game_board[1][1] =="O" and game_board[2][2] == "O":
        if (p==1):
            print("Player 2 wins!!!🎉")
        else:
            print("Player wins!!!🎉")
        mytime()
        exit()
    
    elif game_board[0][2] == "O" and game_board[1][1] =="O" and game_board[2][0] =="O":
        if (p==1):
            print("Player 2 wins!!!🎉")
        else:
            print("Player wins!!!🎉")
        mytime()
        exit()

################### Draw
    c= 0
    for col in range(3):
        for row in range(3):
           if game_board [row][col] != "_":
               c+=1
    if c == 9 : 
      print ("~~~~ DRAW!!!💢~~~~")
      mytime()
      exit()
#########################################################################
    
game_board = [["_" , "_" , "_" ],
              ["_" , "_" , "_" ],
              ["_" , "_" , "_" ]]

show()
       
print("How do you like to play? \n Enter the number.")
print("1. Player VS player")
print("2. Player VS cpu")

p = int(input())

#player VS player
if (p==1):

    while True:

        print("▶ Player 1")

        while True:
            row = int(input("Enter the row:"))
            col = int(input("Enter the col:"))

            if (0<=row<=2) and (0<=col<=2):
                if game_board[row][col]=="_":
                    game_board[row][col] = "X"
                    show()
                    break

                else:
                    print("Already selected!!!🚫")

            else:
                print("The entered value is invalid!!!🚫")  

        check_game()

        print("▶ Player 2")

        while True:
            row = int(input("Enter the row:"))
            col = int(input("Enter the col:"))

            if (0<=row<=2) and (0<=col<=2):
                if game_board[row][col]=="_":
                    game_board[row][col] = "O"
                    show()
                    break

                else:
                    print("Already selected!!!🚫")

            else:
                print("The entered value is invalid!!!🚫")
        check_game()

#Player VS cpu
if (p==2):

    while True:

        print("▶ CPU")

        while True:
            row = random.randint(0,2)
            col = random.randint(0,2)

            if game_board[row][col]=="_":
                game_board[row][col] = "X"
                show()
                break

            else:
                print("Already selected!!!🚫")  

        check_game()

        print("▶ Player")

        while True:
            row = int(input("Enter the row:"))
            col = int(input("Enter the col:"))

            if (0<=row<=2) and (0<=col<=2):
                if game_board[row][col]=="_":
                    game_board[row][col] = "O"
                    show()
                    break

                else:
                    print("Already selected!!!🚫")

            else:
                print("The entered value is invalid!!!🚫")
            
        print("///////////////////////////////////")
        show()
        check_game()