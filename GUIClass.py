# Hope Trygstad
# class for  Othello Game

from graphics import *
from ButtonClass import Button


class GUI:
    
    def __init__(self):
        self.win = GraphWin("Othello!!", 700, 800)
        self.win.setCoords(-1.5, -2.5, 8.5, 8.5)
        self.win.setBackground("grey")
        
        self.boardRect = Rectangle(Point(-0.5, -0.5), Point(7.5,7.5))
        self.boardRect.setFill("green")
        self.boardRect.draw(self.win)
        for i in range(8):
            horiz = Line(Point(-0.5, i-0.5), Point(7.5, i-0.5))
            horiz.draw(self.win)
            vert = Line(Point(i-0.5, 7.5), Point(i-0.5, -0.5))
            vert.draw(self.win)
            
                           
        self.messageBox = Rectangle(Point(-0.5, -0.75), Point(7.5, -2))
        self.messageBox.draw(self.win)
        self.quitButton = Button(self.win, Point(2,8), 1.5, 0.75, "Click to Quit")
        self.quitButton.activate()
        self.playAgain = Button(self.win, Point(6,8), 1.5, 0.75, "Play Again")
        self.message = Text(Point(3.5, -1.25), "Hi, Welcome to Othello!")
        self.message.setFill("white")
        self.message.draw(self.win)

    # I dont think the gui can create the pieces because one of the parameters
    # is the gui itself?
##    def createPieces(self):
##        "Sets up the initial pieces on the board"
##        piece1 = Piece(True, 3, 4, self.win, 
##        pass

    def getWin(self):
        return(self.win)

    def drawThing(self, thing, x, y):
        "Draws an object onto the board, with the thing and its coordinates \
        as parameters"
        thing.image.undraw()
        thing.image.draw(self.win)
        pass


    def turn(self):
        "Shows the user all legal squares, lets them choose their move, \
        does the move in the board, then animates that the AI did in \
        response"
        pass


    def __animate_AI(self):
        "shows the user what move the AI did"
        pass

    def __showAllowedMoves(self, moves):
        "Given the valid moves that are passed in to the function as parameters,\
        lights them up so the player can select them"
        pass

    def __animatePlayerMove(self, move):
        "animates the turn of the human player. The board calculates what tiles\
        from the computer's team will turn over; this just shows it, with the \
        parameter being what move the player chose"
        pass

##def main():
##    myGUI = GUI()
##    piece1 = Piece(True, 3, 4, myGUI)
##
##main()
    
