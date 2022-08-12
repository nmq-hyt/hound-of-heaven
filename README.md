This program implements the classical strategy game, hounds and hare. See https://en.wikipedia.org/wiki/Hare_games#Hare_and_Hounds for the rules.
You can run the game by downloading the zip file, extracting it wherever suits, and invoking

python3 main.py

Works on Linux-like systems only, for the moments.

Or, if you don't want to click the link:
    One player represents the three Hounds, which try to corner the other player's Hare as it seeks to win by escaping them.
    The Hounds move first. Each player can move one piece one step in each turn. The Hounds can only move forward or diagonally (left to right) or vertically (up and down). The Hare can move in any direction.
    The Hounds win if they "trap" the Hare so that it can no longer move.
    The Hare wins if it "escapes" (gets past all the Hounds).
    
I've yet to implement the anti-stalling rule. I'll do that at some point.

You interact with any hound or hare by clicking on it. Any legal moves will be shown in green, any illegal moves in red.
You can reset the board to the default setting by clicking reset.

More development to come.
