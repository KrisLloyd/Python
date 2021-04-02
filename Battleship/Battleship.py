# Imports
from random import randint
import os

# Functions
def print_board(board, turn):
    os.system('cls' if os.name=='nt' else 'clear')
    print(" Battleship! ".center(22, "-"))
    print("----------------------")
    newline()
    print("      1  2  3  4  5")
    print("     ---------------")
    for row in range(len(board)):
        print("  {} | ".format(row + 1) + "  ".join(board[row]))
    newline()
    print("Turn {}".format(turn + 1))
    newline()

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

def getNum(s):
  while True:
      num = input(s)
      if num.lower() == 'x':
        return -1
      if num.isnumeric() and int(num) in range(1,6):
        num = int(num)
        break
  return num - 1

def newline():
    print()

# Initial Setup
def setup():
    board = []
    ships = []
    for x in range(5):
        board.append(["O"] * 5)
    ship_row = random_row(board)
    ship_col = random_col(board)
    ships.append([ship_row, ship_col])

    while True:
        ship2_row = random_row(board)
        ship2_col = random_col(board)
        if ship2_row != ship_row and ship2_col != ship_col:
            ships.append([ship2_row, ship2_col])
            break
    return board, ships

# Game play
def play():
    board, ships = setup()
    for turn in range(8):
      while True:
          print_board(board, turn)
          guess_row = getNum("Enter a Row: ")
          if guess_row == -1:
              return False
          guess_col = getNum("Enter a Col: ")
          if guess_col == -1:
              return False
          if board[guess_row][guess_col] == "O":
              break
          input("You've already tried these coordinates. (Press any key to try again)")

      if [guess_row, guess_col] in ships:
          ships.remove([guess_row, guess_col])
          board[guess_row][guess_col] = "H"
          print_board(board, turn)
          input("\nYou sunk my battleship!\n(Press any key to continue)")
          if len(ships) <= 0:
              newline()
              break
      else:
          board[guess_row][guess_col] = "X"
          print_board(board, turn)
          input("\nMissed!\n(Press any key to continue)")

    # End of Game
    if len(ships) > 0:
        print("Game over!")
        print("There were still {} ships left.".format(len(ships)))
        for i in range(len(ships)):
            print("Remaining ship #{} was at x: {} and y: {}".format(i + 1, ships[i][0] + 1, ships[i][1] + 1))
    else:
        print("Congratulations, you won!")
    option = input("Play again? ('y' to play again, any other input for 'n'): ")
    if option.lower() == 'y':
        return True
    else:
        return False

if __name__ == "__main__":
    x = True
    while x:
        x = play()
    print("Thanks for playing!")
