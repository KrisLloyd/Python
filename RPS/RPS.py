"""This is a basic Rock Paper Scissor game. The user will be prompted for a selection, the computer will choose a random selection, and the results will be compared. The winner of the comparison will be displayed on the screen."""


from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]
message = {"tie" : "It was a tie.", "won" : "You won!", "lost" : "The computer wins!"}

def decide_winner(user_choice, computer_choice):
  print "Your choice was: " + str(user_choice)
  print "Computer choice was: " + str(computer_choice)
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]
    
    
def play_RPS():
  user_choice = raw_input("Please select either ROCK, PAPER, or SCISSORS: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
  
  
play_RPS()
