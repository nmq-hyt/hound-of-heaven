from gamestate.BoardNodeClass import *
from collections import deque
import tkinter as tk
from gamestate.TurnCounter import TurnCounter
from time import sleep
class Board():
    """A undirected graph class to represent a board state"""

    def __init__(self):
        """Initiliaze a default board, using adjacency lists for our 
        representation of the board structure"""
        self.zeroth = BoardNode(State.Hound,0,{'x':80, 'y':175})
        self.first = BoardNode(State.Hound,1,{'x':180, 'y':30})
        self.second = BoardNode(State.Empty,2,{'x':180, 'y':175})
        self.third = BoardNode(State.Hound,3,{'x':180, 'y':315})
        self.fourth = BoardNode(State.Empty,4,{'x':300, 'y':30})
        self.fifth = BoardNode(State.Empty,5,{'x':300, 'y':175})
        self.sixth = BoardNode(State.Empty,6,{'x':300, 'y':315})
        self.seven = BoardNode(State.Empty,7,{'x':420, 'y':30})
        self.eight = BoardNode(State.Empty,8,{'x':420, 'y':175})
        self.nine = BoardNode(State.Empty,9,{'x':420, 'y':315})
        self.ten = BoardNode(State.Hare,10,{'x':520, 'y':175})
        self.adjacenyList = {
            0:[self.first,self.second,self.third], 
            1:[self.zeroth,self.second,self.fourth,self.fifth], 
            2:[self.zeroth,self.first,self.third,self.fifth],
            3:[self.zeroth,self.second,self.fifth,self.sixth],
            4:[self.first,self.fifth,self.seven],
            5:[self.first,self.second,self.third,self.fourth,self.sixth,self.seven,self.eight,self.nine],
            6:[self.third,self.fifth,self.nine],
            7:[self.fourth,self.fifth,self.eight,self.ten],
            8:[self.seven,self.fifth,self.nine,self.ten],
            9:[self.sixth, self.fifth,self.eight,self.ten],
            10:[self.seven,self.eight,self.nine]
            }
        self.nodeList = [self.zeroth,
                        self.first,
                        self.second,
                        self.third,
                        self.fourth,
                        self.fifth,
                        self.sixth,
                        self.seven,
                        self.eight,
                        self.nine,
                        self.ten]
        self.zeroth.neighbours = self.adjacenyList[0]
        self.first.neighbours = self.adjacenyList[1]
        self.second.neighbours = self.adjacenyList[2]   
        self.third.neighbours = self.adjacenyList[3]
        self.fourth.neighbours = self.adjacenyList[4]
        self.fifth.neighbours = self.adjacenyList[5]
        self.sixth.neighbours = self.adjacenyList[6]
        self.seven.neighbours = self.adjacenyList[7]
        self.eight.neighbours = self.adjacenyList[8]   
        self.nine.neighbours = self.adjacenyList[9]
        self.ten.neighbours = self.adjacenyList[10]
        self.winSleepTime = float(5)
        self.turnCounter = TurnCounter()

class BoardWindow():
    """ A graphical representation of the board state"""

    def __init__(self):
        """Initiliaze the graphical board"""
        self.board = Board()
        self.adjacenyList = self.board.adjacenyList
        self.main_window = tk.Tk()
        self.main_window.resizable(width=False, height=False)
        self.main_window.title("Hounds of Heaven")
        self.window_frame = tk.Frame(
            master = self.main_window,
            relief=tk.RAISED,
            borderwidth=2,
            width=750,
            height=750)
        self.canvas = tk.Canvas(width=750,height=750,background='grey')
        self.resetButton = tk.Button(text="Reset", width=5, height=1)
        self.resetButton.place(x=650, y=0)
        self.resetButton.configure(command=self.reset_board)
        self.zerothButton = BoardNodeButton(self, self.board.zeroth)
        self.firstButton = BoardNodeButton(self, self.board.first)
        self.secondButton = BoardNodeButton(self, self.board.second)
        self.thirdButton = BoardNodeButton(self, self.board.third)
        self.fourthButton = BoardNodeButton(self, self.board.fourth)
        self.fifthButton = BoardNodeButton(self, self.board.fifth)
        self.sixthButton = BoardNodeButton(self, self.board.sixth)
        self.seventhButton = BoardNodeButton(self, self.board.seven)        
        self.eightButton = BoardNodeButton(self, self.board.eight)
        self.ninthButton = BoardNodeButton(self, self.board.nine)
        self.tenthButton = BoardNodeButton(self, self.board.ten)
        self.tenthButton.board_node.enabledTruth = False
        self.buttonList = [
            self.zerothButton,
            self.firstButton,
            self.secondButton,
            self.thirdButton,
            self.fourthButton,
            self.fifthButton,
            self.sixthButton,
            self.seventhButton,
            self.eightButton,
            self.ninthButton,
            self.tenthButton
        ]
        for i in self.buttonList:
            i.button.configure(command=i.handle_click)
        self.breadth_first_func(self,self.board.zeroth,self.draw_line_between_nodes)
        self.breadth_first_func(self,self.board.ten,self.draw_line_between_nodes)
        self.breadth_first_func(self,self.board.fifth,self.draw_line_between_nodes)
        self.breadth_first_func(self,self.board.eight,self.draw_line_between_nodes)
        self.status_label = tk.Label(self.main_window,text="Hounds Of Heaven", width =15)
        self.status_label.place(x=300, y = 0)
        self.main_window.geometry('720x480+50+50')
        self.canvas.pack()
        self.lastClicked = None
        self.main_window.mainloop()

# since we can't make an eulerian path through this here graph
# "connected graphs have eulerian cycles iff every vertex has an even degree"
# and since i needed to practice writing bst/dst anyway
# here's breadth first search that accepts a function that i can use to navigate around the graph
    def breadth_first_func(self,graph,node,func):
        for button in self.buttonList:
            button.board_node.color = "white"
        queue = deque([])
        node.color = "grey";
        queue.appendleft(node)
        while (len(queue) != 0):
            temp = queue.popleft()
            for node in graph.adjacenyList.get(temp.board_pos):
                if node.color == "white":
                    node.color = "grey"
                    func(temp,node)
                    queue.appendleft(node)
            temp.color = "black"

    def draw_line_between_nodes(self,first,second):
        self.canvas.create_line((first.x + (first.x + 60)) / 2, (first.y + (first.y + 70)) / 2, (second.x + (second.x + 60)) / 2, (second.y + (second.y +70)) / 2)

    def swap_places(self,position_1,position_2):
        currentHare = None
        currentHounds = []
        for node in self.buttonList:
            if (node.board_node.state == State.Hare):
                currentHare = node
            if (node.board_node.state == State.Hound):
                currentHounds.append(node)
        button_1 = self.buttonList[position_1.board_node.board_pos]
        button_2 = self.buttonList[position_2.board_node.board_pos]
        temp1 = button_1.board_node.state
        temp2 = button_2.board_node.state
        button_1.board_node.state = temp2
        button_2.board_node.state = temp1
        button_1.button.configure(image=button_1.button_image_list[temp2])
        button_2.button.configure(image=button_2.button_image_list[temp1])
        self.reset_colors()
        self.board.turnCounter.incrementcount()
        for node in self.buttonList:
            if (node.board_node.state == State.Hare):
                currentHare = node
            if (node.board_node.state == State.Hound):
                currentHounds.append(node)
        self.hare_or_hound(self.board.turnCounter.whoseTurn())
        print(self.is_game_over(currentHounds,currentHare))
       
    def reset_colors(self):
        for node in self.buttonList:
            node.button.configure(bg='red')

    def show_moves(self, moves):
        self.reset_colors()
        if moves == []:
            return None
        for key, value in moves.items():
            if value == True:
                self.buttonList[key].button.configure(bg='green')

    def reset_board(self):
        self.reset_colors()
        for node in self.buttonList:
            node.board_node.state = State.Empty
        self.buttonList[0].board_node.state=State.Hound  
        self.buttonList[1].board_node.state=State.Hound
        self.buttonList[3].board_node.state=State.Hound
        self.buttonList[10].board_node.state=State.Hare
        for node in self.buttonList:
            node.redraw_button()
        self.board.turnCounter.count = 0
        self.hare_or_hound(0)
        
    def hare_or_hound(self,turnNumber):
        if turnNumber == 0:
            self.status_label.configure(text="Hounds' Turn")
            for node in self.buttonList:
                if node.board_node.state == State.Hare:
                    node.board_node.enabledTruth = False
                elif node.board_node.state == State.Hound:
                    node.board_node.enabledTruth = True                
        if turnNumber == 1:
            self.status_label.configure(text="Hares' Turn")
            for node in self.buttonList:
                if node.board_node.state == State.Hound:
                    node.board_node.enabledTruth = False
                elif node.board_node.state == State.Hare:
                    node.board_node.enabledTruth = True
        self.breadth_first_func(self,self.board.zeroth,self.debug_enabled_state)
        
    def is_game_over(self,hounds, hare):
        result = hare.board_node.check_moves_hare()
        # if the hare can't make any moves, it is trapped, and loses
        if (True not in result.values()):
            self.reset_board()
            return "Hounds"
        hounds_passed = []
        for hound in hounds:
            hound.enabledTruth = True;
            if (hound.board_node.x > hare.board_node.x):
                hounds_passed.append(hound);
            hound.enabledTruth = False;
        if (len(hounds_passed) == 3):
            self.reset_board()
            return "Hares"
        else:
            return "Continue"