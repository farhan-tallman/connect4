"""
Author: Farhan  N.
Date 19 Jan 2021
------------------

Project #1: A Simple Game

Details:
Have you ever played "Connect 4"? It's a popular kid's game by the Hasbro company.
In this project, your task is create a Connect 4 game in Python.
Before you get started, please watch this video on the rules of Connect 4:

https://youtu.be/utXzIFEVPjA

Once you've got the rules down, your assignment should be fairly straightforward.
You'll want to draw the board, and allow two players to take turns placing their pieces on the board
(but as you learned above, they can only do so by choosing a column, not a row).
The first player to get 4 across or diagonal should win!

Normally the pieces would be red and black, but you can use X and O instead.

Extra Credit:

Want to try colorful pieces instead of X and O? First you'll need to figure out how to import a package
like termcolor into your project. We're going to cover importing later in the course,
but try and see if you can figure it out on your own. Or you might be able to find unicode characters to use instead,
depending on what your system supports. Here's a hint: print(u'\u2B24')
"""

ROWS = 11
COLUMNS = 13

####################
# Global Variables
####################

GameEnd = False  # indicates that the game has ended to end the forever loop
GameList = [[" ", " ", " ", " ", " ", " ", " "],  # 7 columns and 6 rows
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " "]]


###########################################
# Function to draw the board on the screen
###########################################


def draw_board():
    global GameList
    for row in range(ROWS):
        for column in range(COLUMNS):
            if row % 2 == 0:  # if it is even row
                if column % 2 == 0:  # if it is even column
                    if column != COLUMNS - 1:  # if it is not the last column
                        print(GameList[int(row / 2)][int(column / 2)], end="")  # print space without newline
                    else:  # otherwise
                        print(GameList[int(row / 2)][int(column / 2)])  # print space along with newline
                elif column != COLUMNS - 1:  # if it is odd column but not the last
                    print("|", end="")  # print | without newline
                else:
                    print("|")  # otherwise print with newline
            else:  # if the row is odd
                if column != COLUMNS - 1:  # and the column is not last
                    print("-", end="")  # print "-" without newline
                else:  # otherwise
                    print("-")  # print "-" with newline
    return True


##############################################
# Function to check if 4 places are connected
##############################################

def check_connect():
    global GameEnd
    global GameList

    matchPlayer = matchHorizontal("X")
    if matchPlayer == 4:
        print("\nPlayer 1 is the winner!")
        GameEnd = True
        return

    matchPlayer = matchHorizontal("O")
    if matchPlayer == 4:
        print("\nPlayer 2 is the winner!")
        GameEnd = True
        return

    matchPlayer = matchVertical("X")
    if matchPlayer == 4:
        print("\nPlayer 1 is the winner!")
        GameEnd = True
        return

    matchPlayer = matchVertical("O")
    if matchPlayer == 4:
        print("\nPlayer 2 is the winner!")
        GameEnd = True
        return

    matchPlayer = matchDiagonal("X")
    if matchPlayer:
        print("\nPlayer 1 Diagonal Win!")
        GameEnd = True
        return

    matchPlayer = matchDiagonal("O")
    if matchPlayer:
        print("\nPlayer 2 Diagonal Win!")
        GameEnd = True
        return


# LOOK FOR HORIZONTAL MATCH OF ENTERED SYMBOL
# -------------------------------------------
def matchHorizontal(symbol):
    global GameEnd
    global GameList
    matchPlayerH = 0  # Counter to count adjacent match

    for ro in range(6):  # traverse through each row
        for co in range(7):  # traverse through each column in the row
            if GameList[ro][co] == symbol:  # if the element is 'X'
                matchPlayerH += 1  # increment the match variable to indicate one is found
                if matchPlayerH == 4:  # means 4 'X' in a row have been found
                    return matchPlayerH
            else:  # means 4 matches were not found
                matchPlayerH = 0  # reset the counter


# LOOK FOR VERTICAL MATCH OF ENTERED SYMBOL
# -----------------------------------------
def matchVertical(symbol):
    global GameEnd
    global GameList
    matchPlayer = 0

    for co in range(7):  # traverse through each column
        for ro in range(6):  # traverse through each row in the column
            if GameList[ro][co] == symbol:  # if the element is 'X'
                matchPlayer += 1  # increment the match variable to indicate one is found
                if matchPlayer == 4:  # means 4 'X' in a column have been found
                    return matchPlayer
            else:  # means 4 matches were not found
                matchPlayer = 0  # reset the counter
    return 0


# Function to check right to left diagonal
# ------------------------------------------
def matchDiagonal(symbol):
    matchPlayer = 0
    sides = ["R2L", "L2R"]

    # the following 4 level nested for loop is for traversing through all
    # possible diagonals that can be formed from right to left and then
    # from left to right with 4 elements
    # the columns range from  3 to 6 for right to left comparison
    # and from 0 to 3 for left to right

    for side in sides:  # this loop will run twice, once for diagonals from right to left and
        # once for diagonals from left to right
        if side == "R2L":  # Check diagonals from right to left
            column = 3
        else:  # side == "L2R":   check diagonals from left to right
            column = 0

        for row in range(3):
            for i in range(4):
                r = row
                c = column
                # print(side)
                for j in range(4):  # this loop checks for adjacent 4 elements
                    if GameList[r][c] == symbol:
                        matchPlayer += 1
                    # print(r, c)
                    r += 1
                    if side == "R2L":
                        c -= 1
                    else:
                        c += 1
                if matchPlayer == 4:  # 4 adjacent matches have been found
                    return True
                matchPlayer = 0  # otherwise reset
                column += 1  # start from next column in the same row
                # print("\n")
            if side == "R2L":  # right to left diagonals
                column = 3  # Reset column to 3 and start from next Row
            else:  # left to right diagonals
                column = 0  # Reset column to 0 and start from next Row

    return False


################
# Main
################

player = 1
count = 0
while not GameEnd:  # condition to end game
    print("\nPlayer", player)
    col = int(input("Enter the column Number: "))
    col -= 1  # because user will put 1 in place of 0th column

    # check for invalid data
    print(col)
    if col > 6 or col < 0:
        print("Invalid Column, Try Again!")
        continue

    if player == 1:
        for r in range(6, 0, -1):  # count upwards from last row (row 6)
            if GameList[r - 1][col] == " ":  # if it is empty
                GameList[r - 1][col] = "X"  # fill it with 'X'
                break  # so that no other rows are filled
        player = 2
    else:
        for r in range(6, 0, -1):
            if GameList[r - 1][col] == " ":
                GameList[r - 1][col] = "O"
                break
        player = 1
    count += 1
    draw_board()
    check_connect()
