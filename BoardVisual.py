from tkinter import *
from Board import *

class BoardVisual:
    """
               BoardVisual class is a visualisation of the  board on which the game takes place
               It mainly uses tkinter
               Every spot on the board is a tkinter button
    """

    def __init__(self, root, frame, board):
        """
                Constructor of BoardVisual class.
                    :param root:(Tk) size of the board (length of columns and rows)
                    :param frame:(tkinter Frame) size of the board (length of columns and rows)
                    :param board:(list) board representation
        """
        self.bframe = frame
        self.root = root
        self.board = board
        self.initialize()
        self.bframe.grid(row=5, column=5)


    def initialize(self):
        """
                This function initializes the view of the board
                It first creates number labels around the board using tkinter Label,
                then creates visualisation of the board itself using tkinter Buttons with no text on
                along with the special spots which are 'get bonus' or a center of the board
                (creating them with different colours and text on)
                :return: void - only changing the object and putting it in the Frame
        """
        #creating labels around the board
        for col in range(1, 16):
            label = Label(self.bframe, text=str(col))
            label.grid(row=0, column=col)
        for row in range(1, 16):
            label = Label(self.bframe, text=str(row))
            label.grid(row=row, column=0)
        #creating visualisation of the board itself
        for row in range(1, 16):
            for col in range(1, 16):
                button = Button(self.bframe, height=3, width=3, bg="bisque", fg="gray1", text=" ")
                button.grid(row=row, column=col)
                self.board[row - 1][col - 1] = button
        #special tiles
        self.board[7][7]["bg"] = "salmon"       #center of the board
        self.board[7][7]["text"] = "#"
        #LX means this place is a bonus giver (you get a bonus points if you place the letter on them)
        self.board[0][0]["bg"] = "light blue"
        self.board[0][0]["text"] = "L5"
        self.board[14][14]["bg"] = "light blue"
        self.board[14][14]["text"] = "L5"
        self.board[0][14]["bg"] = "light blue"
        self.board[0][14]["text"] = "L5"
        self.board[14][0]["bg"] = "light blue"
        self.board[14][0]["text"] = "L5"

        self.board[3][3]["bg"] = "pale green"
        self.board[3][3]["text"] = "L4"
        self.board[11][3]["bg"] = "pale green"
        self.board[11][3]["text"] = "L4"
        self.board[3][11]["bg"] = "pale green"
        self.board[3][11]["text"] = "L4"
        self.board[11][11]["bg"] = "pale green"
        self.board[11][11]["text"] = "L4"

        self.board[7][3]["bg"] = "pale violet red"
        self.board[7][3]["text"] = "L3"
        self.board[3][7]["bg"] = "pale violet red"
        self.board[3][7]["text"] = "L3"
        self.board[11][7]["bg"] = "pale violet red"
        self.board[11][7]["text"] = "L3"
        self.board[7][11]["bg"] = "pale violet red"
        self.board[7][11]["text"] = "L3"

        self.board[5][5]["bg"] = "plum2"
        self.board[5][5]["text"] = "L2"
        self.board[5][9]["bg"] = "plum2"
        self.board[5][9]["text"] = "L2"
        self.board[9][5]["bg"] = "plum2"
        self.board[9][5]["text"] = "L2"
        self.board[9][9]["bg"] = "plum2"
        self.board[9][9]["text"] = "L2"


