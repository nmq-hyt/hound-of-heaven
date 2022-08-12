from BoardClass import *
import pathlib
class Hare():
    """ Represents ability for agent to move around the game board"""

    def __init__(self,board,current_board_node):
        self.current_board_node = current_board_node
        self.board = board
        self.moveList = []
        self.validMoves ={}
            