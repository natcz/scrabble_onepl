from random import randint, choice

class Letters:
    """
        Letters class stores information about letters.
    """

    def __init__(self):
        """
            Constructor of Letters class.
            bag:(dictionary) key: letter val: [points you get for the letter, number of tiles in the bag]

        """
        self.bag = dict()
        self.startLetters()

    def startLetters(self):
        """
            This function creates dictionary with info about letters
            :return: void - only changing the object
        """

        self.bag['A'] = [1,9]
        self.bag['B'] = [3,2]
        self.bag['C'] = [3,2]
        self.bag['D'] = [2,4]
        self.bag['E'] = [1,12]
        self.bag['F'] = [4,2]
        self.bag['G'] = [2,3]
        self.bag['H'] = [4,2]
        self.bag['I'] = [1,9]
        self.bag['J'] = [8,1]
        self.bag['K'] = [5,1]
        self.bag['L'] = [1,4]
        self.bag['M'] = [3,2]
        self.bag['N'] = [1,6]
        self.bag['O'] = [1,8]
        self.bag['Q'] = [10,1]
        self.bag['P'] = [3,2]
        self.bag['R'] = [1,6]
        self.bag['S'] = [1,4]
        self.bag['T'] = [1,6]
        self.bag['U'] = [1,4]
        self.bag['W'] = [4,2]
        self.bag['V'] = [4,2]
        self.bag['X'] = [8,1]
        self.bag['Y'] = [4,2]
        self.bag['Z'] = [10,1]

    def getLetters(self):
        """
            This function returns bag of letters
            :return: dict  - dict with info about letters
        """
        return self.bag

    def makeDict(self):
        """
            This function makes a  set of words from the english dictionary file.
            File is from  https://www.mit.edu/~ecprice/wordlist.10000
            :return: set - set of english words
        """

        try:
            d_file = open('dictionary')
            eng_dict = set()
            for line in d_file:
                line = line.strip()
                eng_dict.add(line.upper())
            return eng_dict
        except IOError:
            print("No such a file found")









