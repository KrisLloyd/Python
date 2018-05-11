#Imports
from random import randint
import os
board = []

#Function declarations
for x in range(5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

#System variables
ship_row = random_row(board)
ship_col = random_col(board)
while (True):
    ship2_row = random_row(board)
    ship2_col = random_col(board)
    if ship2_row != ship_row and ship2_col != ship_col:
        break
ships = 2

#Game play
for turn in range(8):
  os.system('cls' if os.name=='nt' else 'clear')
  print "Welcome to Battleship!"
  print "----------------------------"
  print
  print_board(board)
  print
  print "Turn ", turn + 1
  print
  while (True):
      guess_row = int(raw_input("Enter a Row: "))
      if guess_row in range(10):
          break
  while (True):
      guess_col = int(raw_input("Enter a Col: "))
      if guess_col in range(10):
          break

  if (guess_row == ship_row and guess_col == ship_col) or (guess_row == ship2_row and guess_col == ship2_col):
    print "Congratulations! You sunk my battleship!"
    if guess_row == ship_row and guess_col == ship_col:
        board[guess_row][guess_col] = "H"
        ships -= 1
    else:
        board[guess_row][guess_col] = "H"
        ships -= 1
    if ships == 0:
        break
  else:
    if guess_row not in range(5) or guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif(board[guess_row][guess_col] == "X"):
      print "You guessed that one already."
      turn - 1
    else:
      print "You missed!"
      board[guess_row][guess_col] = "X"
    if turn == 7:
      print "Game Over"
      print "Ship 1: [" + str(ship_row) + ", " + str(ship_col) + "]"
      print "Ship 2: [" + str(ship2_row) + ", " + str(ship2_col) + "]"
      break
  raw_input()
