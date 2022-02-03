from collections import defaultdict as dd
from Board import *
from CheckBoard import *


class Hint:
    """
            Hint class is a tool to generate word (and starting coordinates)
            which can be used by a player. It runs when player hit the "HINT" button.
    """

    def __init__(self, board, eng_dict, rack):
        """
                Constructor of Hint class.
                    :param board:(list) representation of the board
                    :param eng_dict:(set) set of english words
                    :param rack:(list) player's rack
        """
        self.board = board
        self.eng_dict = eng_dict
        self.rack = rack

    def similarLetters(self, word1, word2):
        """
                This function calculates number of letters that are in both word1 and word2.
                It creates a itertools default dictionary for both word1 and word 2
                where key: letter val: number of instances of letters and then counts how many letters
                are the same in both.
                :param word1:(string) first word
                :param word2:(string) second word
                :return: int - number of common letters
        """
        w1 = dd(lambda: 0)
        w2 = dd(lambda: 0)
        counter = 0                        #creating a deafault dict for each word where
        for letter in word1:               #key: letter val: number of instances of letters
            w1[letter] += 1
        for letter in word2:
            w2[letter] += 1
        for key, val in w1.items():        #counting how many letters are the same in word1 and word2
            counter += min(val, w2[key])
        return counter

    def freeUp(self, row, col):
        """
            This function checks how much free space is above the letter on the board
            :param row:(int) row of the board  in which the letter is
            :param col:(int) column of the board  in which the letter is
            :return: int - number of blank space
        """
        counter = 0
        i = row - 1
        while i >= 0:
            if self.board[i][col] == '_':
                counter += 1
            else:
                break
            i -= 1
        return counter

    def freeLeft(self, row, col):
        """
                   This function checks how much free space is on the left side of  the letter on the board
                   :param row:(int) row of the board  in which the letter is
                   :param col:(int) column of the board  in which the letter is
                   :return: int - number of blank space
        """
        counter = 0
        i = col - 1
        while i >= 0:
            if self.board[row][i] == '_':
                counter += 1
            else:
                break
            i -= 1
        return counter

    def freeDown(self, row, col):
        """
                   This function checks how much free space is under the letter on the board
                   :param row:(int) row of the board  in which the letter is
                   :param col:(int) column of the board  in which the letter is
                   :return: int - number of blank space
        """
        counter = 0
        i = row + 1
        while i < len(self.board):
            if self.board[i][col] == '_':
                counter += 1
            else:
                break
            i += 1
        return counter

    def freeRight(self, row, col):
        """
                   This function checks how much free space is on the right side of  the letter on the board
                   :param row:(int) row of the board  in which the letter is
                   :param col:(int) column of the board  in which the letter is
                   :return: int - number of blank space
        """
        counter = 0
        i = col + 1
        while i < len(self.board):
            if self.board[row][i] == '_':
                counter += 1
            else:
                break
            i += 1
        return counter

    def findHint(self):
        """
                This function finds word and its letter coordinates which player can make a move with.
                It takes words from the english word set (eng_dict) that have a lot of the same letters
                with player's rack and tries to put them around letters already on the board.
                :return: string,list -  word, list of letter coordinates
        """

        list_eng_dict = list(self.eng_dict)    #filtering the list of english words
        list_eng_dict = [word for word in list_eng_dict if len(word) <= 5 and len(word) >= 2]
        # sorting words by the number of similar letters with the letters in the player's rack
        list_eng_dict.sort(key=lambda x: self.similarLetters(x, self.rack), reverse=True)

        board_letters_coords = dd(list) #key: letter of the board val: list of lists of information about the letter
        s = len(self.board)

        for i in range(s):
            for j in range(s):
                if self.board[i][j] != '_':
                    up = self.freeUp(i, j)        #how many free tiles above the letter(int)
                    down = self.freeDown(i, j)    #how many free tiles under the letter(int)
                    right = self.freeRight(i, j)  #how many free tiles on the right side of the letter(int)
                    left = self.freeLeft(i, j)    #how many free tiles on the left side of theletter(int)
                    #adding information about the letter [row, column,up,down,right,left]
                    board_letters_coords[self.board[i][j]].append([i, j, up, down, right, left])



        for word in list_eng_dict:                          #getting the word out of the eng_dict
            w = set(word)
            for letter in board_letters_coords.keys():      #getting the letter out of the board
                if letter in w:                             #checking if the letter appears in the word
                    rack = self.rack[:]
                    rack.append(letter)                     #adding letter to the list of letters in the player's rack
                    if self.similarLetters(word,rack) < len(word):      #you cannot build word with given letters
                        continue
                    else:
                        ind = word.index(letter)            #index of the letter in the word
                        l_left = ind                        #number of letters on the left side of the letter in word
                        r_left = len(word) - ind - 1        #number of letters on the right side of the letter in word
                        for i in range(len(board_letters_coords[letter])):
                            #getting out the info about letter
                            free_up = board_letters_coords[letter][i][2]
                            free_down = board_letters_coords[letter][i][3]
                            free_right = board_letters_coords[letter][i][4]
                            free_left = board_letters_coords[letter][i][5]
                            x = board_letters_coords[letter][i][0]
                            y = board_letters_coords[letter][i][1]
                            #checking if there is enough of free space to place the letters of word around the letter
                            horizon_good = l_left <= free_left and r_left <= free_right
                            vertic_good = l_left <= free_up and r_left <= free_down
                            w_coords = []       #list of word's letters coordinates
                            if horizon_good or vertic_good:
                                if horizon_good:        #horizontal placing (in the row) is possible
                                    i = 0
                                    j = ind
                                    while i < len(word): #saving letters' coordinates
                                        w_coords.append((x,y-j))
                                        j -= 1
                                        i += 1
                                    #checking if placing is possible
                                    if CheckBoard(self.board).checkBoard(self.eng_dict, word, w_coords):
                                        return word, w_coords
                                w_coords = []
                                if vertic_good:     #vertical placing (in the column) is possible
                                    i = 0
                                    j = ind
                                    while i < len(word):  #saving letters' coordinates
                                        w_coords.append((x-j, y))
                                        j -= 1
                                        i += 1
                                    # checking if placing is possible
                                    if CheckBoard(self.board).checkBoard(self.eng_dict, word, w_coords):
                                        return word, w_coords
                            else:
                                continue

        return "", []
