import tkinter as tk
from tkinter import ttk

class State:
    Empty = 0
    Hare = 1
    Hound = 2
    

class StateImageMap:
    theMap= {State.Empty: './assets/images/blank.png', State.Hare: './assets/images/hare.png', State.Hound: './assets/images/hound.png'}
    stringMap = {State.Empty: 'Empty', State.Hare: 'Hare', State.Hound: 'Hound'}

class BoardNode():
    """A class representing an individual board node"""

    def __init__(self,state,board_pos,window_position):
        """Initalize a given node with a state and its neighbors as a list of BoardNodes

        There are three possible states: hare,hound and empty. A whole bunch of game logic interacts with this string.

        The color option is not the actual color of the node (that is handled in BoardNodeButton), but is a string
        used to flag its state in CLRS's version of breadth-first search.

        Buttons are only clickable if they're enabled.
        
        Each board keeps a track of its own position, both in the window and on the game board.

        """
        self.state = state
        self.color  = "white"
        self.enabledTruth = True
        self.board_pos = board_pos
        self.neighbours = []
        self.validDict = {}
        self.window_position = window_position
        self.x = window_position.get('x')
        self.y = window_position.get('y')

    # a utility method to ensure hounds cannot move backwards.
    # this is an illegal move
    # no hound crimes here
    def validate_hound_move(self,Space):
        return (self.x <= Space.x)

    def get_moves(self):
        self.validDict.clear()
        if (self.enabledTruth == False) or (self.state == State.Empty):
            return self.validDict
        if (self.state == State.Hare):
            for node in self.neighbours:
                if node.state == State.Empty:
                    self.validDict[node.board_pos] = True
                elif node.state == State.Hound:
                    self.validDict[node.board_pos] = False      
            return self.validDict
        if(self.state == State.Hound):
            for node in self.neighbours:
                if (node.state == State.Empty) and (self.validate_hound_move(node)):
                    self.validDict[node.board_pos] = True
                if node.state == State.Hound or node.state == State.Hare:
                    self.validDict[node.board_pos] = False
            return self.validDict
        
    def check_moves_hare(self):
        self.validDict.clear()
        for node in self.neighbours:
                if node.state == State.Empty:
                    self.validDict[node.board_pos] = True
                elif node.state == State.Hound:
                    self.validDict[node.board_pos] = False      
                return self.validDict

        

class BoardNodeButton():
    """A class representing a button which has a board node, which handles all of its  graphical functions"""
    
    def __init__(self,board_window,board_node):
        self.board_window = board_window
        self.board_node = board_node
        self.button_image_list = [tk.PhotoImage(file=StateImageMap.theMap[State.Empty], width=55, height=55),tk.PhotoImage(file=StateImageMap.theMap[State.Hare], width=55, height=55),tk.PhotoImage(file=StateImageMap.theMap[State.Hound], width=55, height=55)]
        self.button_image = self.button_image_list[self.board_node.state]
        self.button = tk.Button(width=65, height=65,image=self.button_image, bg='#855907',activebackground='#d99009')
        self.button.configure(bg='red')
        self.button.place(x = self.board_node.window_position.get('x'), y = self.board_node.window_position.get('y'))
        self.x = self.board_node.window_position.get('x')
        self.y = self.board_node.window_position.get('y')

    def redraw_button(self):
        self.button.configure(image=self.button_image_list[self.board_node.state])
    
    def get_moves(self):
        moves_result = self.board_node.get_moves()
        if (moves_result == []):
            self.board_window.show_moves([])
        else:
            self.board_window.show_moves(moves_result)

    def do_move(self,lastClickedButton):
        try:
            lastState = StateImageMap.stringMap[lastClickedButton.board_node.state]
            lastColor = lastClickedButton.button.config()['background'][-1] 
            currentColor = self.button.config()['background'][-1]
            if (lastClickedButton.board_node.enabledTruth == True):
                if (lastColor == 'red') and (lastState != 'Empty') and (currentColor == 'green'):
                    self.board_window.swap_places(lastClickedButton,self)
                    self.board_window.lastClicked = self
            else:
                pass
        except AttributeError:
            print("Nonsense move")

    def handle_click(self):
        current_state = self.board_node.state;
        if current_state == State.Hare or current_state == State.Hound:
            self.board_window.reset_colors()
            self.get_moves()
            self.board_window.lastClicked = self
        elif current_state == State.Empty:
            self.do_move(self.board_window.lastClicked)