[< Back to Python Projects](https://github.com/KrisLloyd/Python#python)
***

# About
Simple battleship game.

# Useage

Run the python script from the command line

```
battleship.py
```

At the game startup, you'll be prompted for a row then a column. If the computer has placed a battleship there, you'll get a hit!

```
You sunk my battleship!
(Press any key to continue)
```

Otherwise it'll be a miss!

```
Missed!
(Press any key to continue)
```

The locations of your guesses will be marked on your map. An **'H'** for a hit, and an **'X'** for a miss. You'll have 8 turns to guess the location of both of the computer's ships. If you don't manage to find them all, their locations will be revealed at the end of the game.

```
Remaining ship #1 was at x: 3 and y: 4
Remaining ship #2 was at x: 1 and y: 2
```

If you try to guess the same location twice, the computer will tell you to try a different location.

```
You've already tried these coordinates.
(Press any key to try again)
```

You can press **'x'** at any time (when asked for input) to exit the game.

# Examples

* Repeated guesses at the same coordinates:

  ```
  ---- Battleship! -----
  ----------------------
  
        1  2  3  4  5
       ---------------
    1 | O  X  O  O  O
    2 | O  O  O  O  X
    3 | O  O  O  O  O
    4 | O  O  O  O  O
    5 | O  X  O  O  O
  
  Turn 4
  
  Enter a Row: 1
  Enter a Col: 2
  You've already tried these coordinates.
  (Press any key to try again)
  ```

* Winning a game:

  ```
  ---- Battleship! -----
  ----------------------
  
        1  2  3  4  5
       ---------------
    1 | O  X  O  H  O
    2 | O  O  X  O  O
    3 | O  O  X  X  O
    4 | O  X  O  O  X
    5 | H  O  O  O  O
  
  Turn 8
  
  
  You sunk my battleship!
  (Press any key to continue)
  
  Congratulations, you won!
  Play again? ('y' to play again, any other input for 'n'):
  ```


