from Sack import *
from random import shuffle


class Rack:
    """
        Rack class is a representation of player's rack.
        (list of letters)

    """

    def __init__(self, sack, max_l):
        """
            Constructor of Rack class.
            :param sack:(list) list of letters available in the game
            rack:(list)  list of letters available to the player
            max_letters:(int) max number of letters in the rack


        """
        self.rack = []
        self.sack = sack
        self.max_letters = max_l
        self.initRack()

    def initRack(self):
        """
            This function initializes the sack
            It gets out random letters from the sack.
            It randomizes letters in the sack using random shuffle.
            :return: void - only changing the object
        """
        sack = self.sack.getSack()
        shuffle(sack)
        for i in range(self.max_letters):
            if self.sack.leftLetters() != 0:  # making sure sack isn't empty
                self.rack.append(sack[i])
                self.sack.remove(sack[i])

    def fillRack(self):
        """
                This function refills the rack to make sure
                it always contains max_l letters
                :return: void - only changing the object
        """
        sack = self.sack.getSack()
        shuffle(sack)
        while len(self.rack) <= self.max_letters and self.sack.leftLetters() > 0:
            self.rack.append(sack[0])
            self.sack.remove(sack[0])

    def exchangeAll(self):
        """
                This function exchanges all the letters in the rack.
                 :return: void - only changing the object
        """
        rack = self.rack[:]
        for i in range(len(rack)):
            self.rack.remove(rack[i])  # removing letters from the rack
            self.sack.append(rack[i])  # adding letters back to the sack
        self.initRack()                # initializing the rack again

    def exchangeOne(self, ind):
        """
            This function exchanges one particular letter.
            :param ind: (int) index of the letter in the rack
            :return: char - new letter
        """
        letter = self.rack[ind]             # getting the info from the index
        self.sack.append(letter)
        new_letter = self.sack.takeLetter()  # taking new letter out of the sack
        self.rack[ind] = new_letter
        self.sack.remove(new_letter)
        return new_letter

    def getRack(self):
        """
            This function returns rack.
            :return: list - rack
        """
        return self.rack

    def remove(self, letter):
        """
                This function removes letter from the rack
                :param letter: (char) letter to remove
                :return: void - only changing the object
        """
        rackset = set(self.rack)
        if letter in rackset:
            self.rack.remove(letter)
        else:
            pass
