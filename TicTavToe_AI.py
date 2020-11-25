# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 06:55:46 2020

@author: nadin
"""
#Tic Tac Toe game, human vs AI on Python.
#In here is an AI that plays tic tac toe 
#and it's goal is to win

#First we start with the board
 
board = [' ' for x in range(10)]
#This function asks for the letter input from the player
# "X"or "O"
def insertLetter(letter, pos):
    board[pos] = letter
#Checkes if there is free space. As in there is no "X" or "O'
def spaceIsFree(pos):
    return board[pos] == ' '
#This creates the board 
def printBoard(board):
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
#function for when there is a winne, with all the possibiliies of how a winner is chosen    
def isWinner(bo, le):
    return (bo[7] == le and bo[8] == le and bo[9] == le) or (bo[4] == le and bo[5] == le and bo[6] == le) or(bo[1] == le and bo[2] == le and bo[3] == le) or(bo[1] == le and bo[4] == le and bo[7] == le) or(bo[2] == le and bo[5] == le and bo[8] == le) or(bo[3] == le and bo[6] == le and bo[9] == le) or(bo[1] == le and bo[5] == le and bo[9] == le) or(bo[3] == le and bo[5] == le and bo[7] == le)

def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')       
        #to avoid crashing for invaid inputs, such as a number spelled out
        #this is using try and accept
        try:
            move = int(move)  #checking if the number typed matches the range of the board 
            if move > 0 and move < 10:
                if spaceIsFree(move): #checking if space if free
                    run = False
                    insertLetter('X', move)
                       #if the test fails these are the outputs
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')
            
  #the different ways how the computer will win
def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]  #if it is blank or the indice is zero and puts it in a list
    move = 0 # a move the computer has no clue about 

    for let in ['O', 'X']:#check if O will win or X will win
        for i in possibleMoves:   
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                move = i
                return move

    cornersOpen = []#fiding if there is any open corners
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)
            
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    if 5 in possibleMoves:#checking if there is any center is open
        move = 5
        return move

    edgesOpen = []   #now check if the rest of the edges are open
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        
    return move

def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0,ln)
    return li[r]
    
#tells you if the board is full so the computer knows when to stop playing
def isBoardFull(board):
    if board.count(' ') > 1:
        return False
    else:
        return True

def main():
    print('Welcome to my first AI game. You will play agaisnt the computer, are you up for the challenge? ')
    printBoard(board)

    while not(isBoardFull(board)):#since the computer is always O, we will only check situations of O winning
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Loser!!! you lost >:)')
            break#Now lets check if the player won

        if not(isWinner(board, 'X')):
            move = compMove()#if the compuer was not able to make a move
            if move == 0:
                print('Tie Game!')
            else:
                insertLetter('O', move)
                print('The very smart computer has placed an \'O\' in a position', move , ':')
                printBoard(board)
        else:
            print('Ummm....I guess it looks like you won. Dont be too happy I went easy on you.')
            break

    if isBoardFull(board):
        print('Tie Game!')

while True:
    answer = input('Do you want to play again? (Y/N)')
    if answer.lower() == 'y' or answer.lower == 'yes' or answer.lower == 'Yes':
        board = [' ' for x in range(10)]
        print('-----------------------------------')
        main()
    else:
        print('I guess you gave up after losing so many times.')
        break