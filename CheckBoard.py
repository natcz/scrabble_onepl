from Board import *
from Word import *


class CheckBoard:
    """
            CheckBoard class is a tool to check if the players move was correct

    """
    def __init__(self, board):
        """
                Constructor of CheckBoard class.
                :param board:(list) board representation
        """
        self.board = board

    def checkRows(self, eng_dict):
        """
                This function checks if all of the words placed in rows of the board are in the eng_dict
                :param eng_dict:(set) english dictionary (set of english words)
                :return: boolean
        """

        s = len(self.board)
        row = 0
        while row < s:
            col = 0                 #column (int)
            while col < s:
                if self.board[row][col] != '_':
                    new_word = ""
                    counter = 0
                    for i in range(col, s):     #searching for a whole word
                        if self.board[row][i] != '_':
                            new_word += self.board[row][i]
                            counter += 1
                        else:
                            if new_word != "" and len(new_word) > 1:   #if we found whole word
                                nw = Word(new_word)
                                #we are checking if it appears in the eng_dict set
                                if not nw.checkWord(eng_dict):         #using Word() method
                                    return False
                            col += counter
                            break
                col += 1
            row += 1
        return True

    def checkColumns(self, eng_dict):
        """
                    This function checks if all of the words placed in columns of the board are in the eng_dict
                    :param eng_dict:(set) english dictionary (set of english words)
                    :return: boolean
        """

        s = len(self.board)
        col = 0
        while col < s:
            row = 0
            while row < s:
                if self.board[row][col] != '_':
                    new_word = ""
                    counter = 0
                    for i in range(row, s):     #searching for a whole word
                        if self.board[i][col] != '_':
                            new_word += self.board[i][col]
                            counter += 1
                        else:
                            if new_word != "" and len(new_word) > 1:  #if we found whole word
                                nw = Word(new_word)
                                #we are checking if it appears in the eng_dict set
                                if not nw.checkWord(eng_dict):        #using Word() method
                                    return False
                            row += counter
                            break
                row += 1
            col += 1
        return True

    def checkBoard(self, eng_dict, word, coords):
        """
                    This function checks if you can place the word with letter coordinates on the board.
                    It uses checkRows and checkColumns.

                    :param eng_dict:(set) english dictionary (set of english words)
                    :param word:(string) english dictionary (set of english words)
                    :param coords:(itertools defaultdictionary)   key: coordinates of the letter (x,y) val: letter
                    :return: boolean
        """

        temp_board = Board(len(self.board))       #temporary board on which we test the placing
        temp_board.board = self.board[:]

        try:
            temp_board.boardUpdate(word, coords)        #using board updating method from Board()
            temp_board_check = CheckBoard(temp_board.board)
            if not temp_board_check.checkRows(eng_dict):
                return False
            elif not temp_board_check.checkColumns(eng_dict):
                return False
            else:
                return True

        except ValueError:
            return False
