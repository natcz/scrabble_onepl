from tkinter import *
from BoardVisual import *
from Board import *
from StartGame import *
from Sack import *
from Player import *
from BoardVisual import *
from GameController import *
from Letters import *

class Main:


    def __init__(self):
        """
                Constructor of Main class.
                        sack:(Sack) representation of bag of letters
                        root:(Tk) tkinter root
                        startframe:(Frame) tkinter Frame displayed when the game starts
                        mainframe:(Frame) tkinter Frame displayed during the game with board, rack and functional buttons
                        player1:(Player) representation of the first player
                        player2:(Player) representation of the second player
                        startgame:(StartGame) object  needed to display an instruction
        """
        self.root = Tk()
        self.startframe = Frame(self.root)
        self.mainframe = Frame(self.root)
        self.sack = Sack()
        self.player1 = Player(self.sack,7,"")
        self.player2 = Player(self.sack,7,"")
        self.startgame = StartGame()
        self.root.title("Scrabble")
        self.root.geometry("1500x900")
        self.startframe.grid(column=0, row=0)
        startLabel = Label(self.startframe, text="Welcome to Scrabble!")
        startLabel.grid(column=3, row=0)
        startButton = Button(self.startframe, text="New game", command=lambda: Main.getNames(self))
        startButton.grid(column=3, row=5)
        instrButton = Button(self.startframe, text="See the instruction", command=lambda: Main.getInstr(self))
        instrButton.grid(column=3, row=8)


    def getInstr(self):
        """
                This function creates a window where the instruction is displayed
                :return: void - only displays text
        """
        instrWindow = Toplevel()
        instr = self.startgame.viewInstruct()
        instrmsg = Message(instrWindow, text=instr)
        instrmsg.grid(column=1, row=1)
        closeinstrButton = Button(instrWindow, text="Ok, I get it", command=instrWindow.destroy)
        closeinstrButton.grid(column=3, row=3)


    def getNames(self):
        """
            This function creates a window where you can input player's names and saves them
            :return: void - only creating tkinter wigets and saving names
        """

        def saveName():
            self.player1.name = name1entry.get()
            self.player2.name = name2entry.get()

        nameWindow = Toplevel()
        name1entry = Entry(nameWindow)
        name1Label = Label(nameWindow, text="Player1")
        name2entry = Entry(nameWindow)
        name2Label = Label(nameWindow, text="Player2")
        #destroing startframe and going to mainframe with letsPlay method
        confirmB = Button(nameWindow, text="Confirm")
        confirmB["command"] = lambda : [saveName(),nameWindow.destroy(),
                                        self.startframe.destroy(),Main.letsPlay(self)]

        name1entry.grid(column=2,  row=1)
        name2entry.grid(column=2, row=3)
        name1Label.grid(column=1, row=1)
        name2Label.grid(column=1, row=3)
        confirmB.grid(column=3, row=3)



    def letsPlay(self):
        """
            Function to menage the game and the wigets like
            functional buttons:
            "HINT", "SKIP", "EXCHANGE ALL" "EXCHENGE ONE", "END MOVE"
            and labels:
            turn label, score label, information about points for letters
            and visualisation of the player's rack.
            :return: void - only creating tkinter wigets
        """

        b = [['' for columns in range(15)] for rows in range(15)]    #represetation of the board
        GameContr = GameController(self.root,self.mainframe,self.sack,self.player1,self.player2)
        board = BoardVisual(self.root,self.mainframe, b)             #visualization of the board
        emptyLabel = Label(self.mainframe,text="     ").grid(column=19, row=1)    #just for good placing
        #fuctional buttons
        skipB = Button(self.mainframe,text="SKIP", width=12)
        skipB["command"] = lambda: GameContr.skip(PScoreLabel,ScoreLabel,TurnLabel,PRackButtons)
        exchangeAllB = Button(self.mainframe,text="EXCHANGE ALL", width=12)
        exchangeAllB["command"] = lambda: GameContr.exchangeAll(PRackButtons)
        exchangeOneB = Button(self.mainframe, text="EXCHANGE ONE", width=12)
        exchangeOneB["command"] = lambda: GameContr.exchangeOne(PRackButtons,board.board
                                                                ,exchangeAllB,exchangeOneB,skipB)
        hintButton = Button(self.mainframe,text="HINT", width=12,state="disabled")
        hintButton["command"] = lambda: GameContr.hint(board,PScoreLabel,ScoreLabel,TurnLabel,PRackButtons)
        endMoveButton = Button(self.mainframe, text="END MOVE", width=12)
        endMoveButton["command"] = lambda: GameContr.endTurn(PScoreLabel,ScoreLabel,TurnLabel,PRackButtons,board.board,
                                                             hintButton,exchangeAllB,exchangeOneB,skipB)
        skipB.grid(column=20, row=7)
        exchangeAllB.grid(column=20, row=8)
        exchangeOneB.grid(column=20, row=9)
        hintButton.grid(column=20, row=10)
        endMoveButton.grid(column=20, row=11)

        #displaying who's turn it is and the score
        TurnLabel = Label(self.mainframe, text="IT'S " + str(self.player1.name).upper() + "'S TURN")
        PScoreLabel = Label(self.mainframe, text=str(self.player1.name).upper() +"'S SCORE:")
        ScoreLabel = Label(self.mainframe, text=str(self.player1.score))
        TurnLabel.grid(column=20, row=2)
        PScoreLabel.grid(column=20, row=3)
        ScoreLabel.grid(column=21, row=3)

        #displaying info about points for letters (letter=points)
        infoL = Label(self.mainframe,text= "POINTS\n"
                                           "FOR LETTERS:")
        infoL.grid(column=30,row=1)
        letters = Letters()
        bag = letters.bag
        i = 0
        for key,val in bag.items():
            if i <= 12:
                LettersL = Label(self.mainframe,text=str(key) + " = " + str(val[0]) + "   ")
                LettersL.grid(column=31, row=2+i)

            else:
                LettersL = Label(self.mainframe, text=str(key) + " = " + str(val[0]))
                LettersL.grid(column=32, row=2 + i-13)
            i += 1


        PRackButtons = []  #buttons representing player's rack
        playerRack = self.player1.rack.getRack()

        emptyL2 = Label( self.mainframe, text="    ").grid(column=22, row=1) #just for placing

        for i in range(len(playerRack)):       #visualizing the rack
            button = Button(self.mainframe, height=3, width=3, bg="bisque", fg="gray1", text=str(playerRack[i]))
            button.grid(column=23+i, row=9)
            PRackButtons.append(button)

        for i in range(len(PRackButtons)):  #enable letters (buttons) to be moved to the board
            PRackButtons[i]["command"] = lambda x=i: GameContr.makeMove(x, board.board,PRackButtons,
                                                                        exchangeAllB,exchangeOneB,skipB)





a=Main()
a.root.mainloop()
