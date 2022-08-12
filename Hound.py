from BoardClass import *
class Hound():
    """ Represents ability for agent to move around the game board"""

    def __init__(self,board,current_board_node):
        self.current_board_node = current_board_node
        self.board = board
        self.moveList = []
        self.validMoves ={}

    def get_moves(self):
        self.moveList = self.board.adjacenyList[self.current_board_node]
        for node in self.moveList:
            if not (node.x < self.current_board_node.x) and node.state == State.Empty:
                self.validMoves[node] = True
            else:
                self.validMoves[node] = False

            