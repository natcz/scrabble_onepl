from Player import *
from tkinter import *


class EndGame:
    """
        EndGame class is used when the game is over

    """
    def __init__(self, player1, player2, root):
        """
            Constructor of EndGame class.
                :param player1:(Player) first player
                :param player2:(Player) second player
                :param root:(Tk) tkinter root
        """
        self.player1 = player1
        self.player2 = player2
        self.root = root

    def bestPlayer(self):
        """
                This function checks which player won
                :return: Player - player that won the game
        """
        score1 = self.player1.getScore()
        score2 = self.player2.getScore()
        if score1 > score2:
            return self.player1
        else:
            return self.player2

    def endWindow(self):
        """
                This function make window appear when the game is over.
                This window contains of a tkinter Message with the info about the winner
                and a tkinter button "EXIT" to end the game (it destroys tk root)
                :return: void - changing the tkinter root
        """
        endWindow = Toplevel()      # creating a Toplevel window
        winner = self.bestPlayer()  # Player() object
        endMsg = Message(endWindow, text="GAME OVER!\n" + "CONGRATULATIONS\n" + str(winner.name).upper())
        exitB = Button(endWindow, text="EXIT")
        exitB["command"] = lambda: self.root.destroy()  # destroys root (whole game window)
        endMsg.grid(column=1, row=1)                    # placing objects inside the window
        exitB.grid(column=2, row=2)
