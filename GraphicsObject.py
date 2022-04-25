# Hope Trygstad

from graphics import *

class Piece:

    def __init__(self, color, y, x):
        self.color = color
        self.x = x
        self.y = y
        self.color = color
        self.circle = Circle(Point(x, y), 0.35)
        if self.color == True:
            self.circle.setFill("black")
        if self.color == False:
            self.circle.setFill("white")


    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)

    def color(self):
        "draws the piece into the GUI, showing a color change if their \
        was one"
        if self.color == True:
            self.circle.setFill("black")
        if self.color == False:
            self.circle.setFill("white")

    def flipPiece(self):
        "Changes the color of the piece. No parameters since it can only change\
        one way"
        if self.color == True:
            self.color = False
        else:
            self.color = True

    def draw(self, win):
        self.circle.draw(win)
    




        

    
