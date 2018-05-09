"""This program asks the user to roll virtual dice, then guess the outcome. If the guess is correct, the user wins, otherwise the computer wins."""

from random import randint
from time import sleep

#Used to get user input for the guess
def get_user_guess():
  guess = int(raw_input("What is your guess? "))
  return guess

#Used to simulate a dice roll
def roll_dice(number_of_sides):
  first_roll = randint(1, number_of_sides)
  second_roll = randint(1, number_of_sides)
  total_roll = first_roll + second_roll
  max_val = (number_of_sides * 2)
  print "The maximum possible value is %d" % (max_val)
  guess = get_user_guess()
  if guess > max_val:
    print "This guess is too large"
  elif guess < 2:
    print "This guess is too low"
  else:
    print "Rolling..."
    sleep(2)
    print "The first roll is %d " % (first_roll)
    sleep(1)
    print "The second roll is %d " % (second_roll)
    sleep(1)
    print "The result: %d" % (total_roll)
    sleep(1)
    if guess == total_roll:
      print "You got it exactly right!"
    elif (total_roll - 1) <= guess <= (total_roll + 1):
      print "You got within 1 of the correct answer, 1/2 points!"
    else:
      print "The Computer wins this round!"
    
#Main game. Runs once.
print "\nWelcome to the NumberGuess game!"
print "--------------------------------"
number_of_sides = int(raw_input("\nHow many sides would you like to have on your dice? "))
roll_dice(number_of_sides)
