'''
Created on Sep 23, 2014

@author: ben
'''
import sys
tictactoe = ["0","0","0","0","0","0","0","0","0"]
def checker(input, player):
    try:
        if player == 1:
            symbol = "X"
        else:
            symbol = "O"
        if tictactoe[input - 1] == "0":
            if input == 1:
                tictactoe[0] = "%s" % symbol
            elif input == 2:
                tictactoe[1] = "%s" % symbol
            elif input == 3:
                tictactoe[2] = "%s" % symbol
            elif input == 4:
                tictactoe[3] = "%s" % symbol
            elif input == 5:
                tictactoe[4] = "%s" % symbol
            elif input == 6:
                tictactoe[5] = "%s" % symbol
            elif input == 7:
                tictactoe[6] = "%s" % symbol
            elif input == 8:
                tictactoe[7] = "%s" % symbol
            elif input == 9:
                tictactoe[8] = "%s" % symbol
        else:
            print "Error! You did not type the correct input. Your move has been canceled as a penalty."
    except:
        print "Error, you entered a number not on the board. Your move has been canceled as a penalty."
playerHasWon = False
def wincheck():
    #horizontals
    if (tictactoe[0] == tictactoe[1] and tictactoe[0] == tictactoe[2]) and (tictactoe[0] is not "0"):
        if tictactoe[0] == "X":
            playerHasWon = True
            print "Player 1 Wins!"
            sys.exit()
        else:
            playerHasWon = True
            print "Player 2 Wins!"
            sys.exit()
    elif (tictactoe[3] == tictactoe[4] and tictactoe[3] == tictactoe[5]) and (tictactoe[3] is not "0"):
        if tictactoe[3] == "X":
            playerHasWon = True
            print "Player 1 Wins!"
            sys.exit()
        else:
            playerHasWon = True
            print "Player 2 Wins!"
            sys.exit()
    elif (tictactoe[6] == tictactoe[7] and tictactoe[6] == tictactoe[8]) and (tictactoe[6] is not "0"):
        if tictactoe[6] == "X":
            playerHasWon = True
            print "Player 1 Wins!"
            sys.exit()
        else:
            playerHasWon = True
            print "Player 2 Wins!"
            sys.exit()
    #verticals
    elif (tictactoe[0] == tictactoe[3] and tictactoe[0] == tictactoe[6]) and (tictactoe[0] is not "0"):
        if tictactoe[0] == "X":
            playerHasWon = True
            print "Player 1 Wins!"
            sys.exit()
        else:
            playerHasWon = True
            print "Player 2 Wins!"
            sys.exit()
    elif (tictactoe[1] == tictactoe[4] and tictactoe[1] == tictactoe[7]) and (tictactoe[1] is not "0"):
        if tictactoe[1] == "X":
            playerHasWon = True
            print "Player 1 Wins!"
            sys.exit()
        else:
            playerHasWon = True
            print "Player 2 Wins!"
            sys.exit()
    elif (tictactoe[2] == tictactoe[5] and tictactoe[2] == tictactoe[8]) and (tictactoe[2] is not "0"):
        if tictactoe[2] == "X":
            playerHasWon = True
            print "Player 1 Wins!"
            sys.exit()
        else:
            playerHasWon = True
            print "Player 2 Wins!"
            sys.exit()
    #diagonals
    elif (tictactoe[0] == tictactoe[4] and tictactoe[0] == tictactoe[8]) and (tictactoe[0] is not "0"):
        if tictactoe[0] == "X":
            playerHasWon = True
            print "Player 1 Wins!"
            sys.exit()
        else:
            playerHasWon = True
            print "Player 2 Wins!"
            sys.exit()
    elif (tictactoe[3] == tictactoe[4] and tictactoe[3] == tictactoe[6]) and (tictactoe[3] is not "0"):
        if tictactoe[3] == "X":
            playerHasWon = True
            print "Player 1 Wins!"
            sys.exit()
        else:
            playerHasWon = True
            print "Player 2 Wins!"
            sys.exit()
    #check for tie here
    else:
        counter = 0
        for x in xrange(9):
            if tictactoe[x] is not "0":
                continue
            else:
                counter += 1
        if counter == 0:
            print "Tie!"
            sys.exit()
def printLine():
    print "%s, %s, %s" % (tictactoe[6], tictactoe[7], tictactoe[8])
    print "%s, %s, %s" % (tictactoe[3], tictactoe[4], tictactoe[5])
    print "%s, %s, %s" % (tictactoe[0], tictactoe[1], tictactoe[2])
player1Input = ""
player2Input = ""
firstMove = input("Player 1, do you want to go first? Type 'Y' for yes, 'N' for no: ")
print "Directions: Use the num pad to select the space you want to move."
while (not playerHasWon):
    if firstMove == "Y":
        player1Input = input("Player 1 Move: ")
        checker(player1Input, 1)
        printLine()
        wincheck()
        if (not playerHasWon):
            player2Input = input("Player 2 Move: ")
            checker(player2Input, 2)
            printLine()
            wincheck()
    else:
        player2Input = input("Player 2 Move: ")
        checker(player2Input, 2)
        printLine()
        wincheck()
        if not (playerHasWon):
            player1Input = input("Player 1 Move: ")
            checker(player1Input, 1)
            printLine()
            wincheck()