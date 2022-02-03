from Word import *


class Board:
    """
           Board class is a representation of the  board on which the game takes place
    """

    def __init__(self, size):
        """
          Constructor of Board class.
              :param size:(int) size of the board (length of columns and rows)
              board: (list of lists)       representation of the board

        """
        self.size = size
        self.board = [['_' for columns in range(size)] for rows in range(size)]

    def boardUpdate(self, new_word, coords):
        """
                This function adds new word on the board
                :param new_word:(string) word which you want to add to the board
                :param coords:(itertools defaultdictionary)   key: coordinates of the letter (x,y) val: letter
                :return: void - only changing the object
        """

        nw = new_word.upper()
        for i in range(len(coords)):
            self.board[coords[i][0]][coords[i][1]] = nw[i]

    def getBoard(self):
        """
                This function gives the board
                :return: list - Board parameter board
        """

        return self.board

    def getcopy(self):
        return self.board[:]
