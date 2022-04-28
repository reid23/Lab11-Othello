# Hope Trygstad

from graphics import *

class Piece:

    def __init__(self, color, y, x):
        """augh added a docstring bc i keep forgetting true vs false, sorry i know im not supposed to touch non-me code

        Args:
            color (bool): true if black, false if white 
            y (int): y location, in window coords
            x (int): x location, in window coords
        """
        self.color = color
        self.x = x
        self.y = y
        self.color = color
        self.circle = Circle(Point(x, y), 0.35)
        if self.color == True:
            self.circle.setFill("black")
        if self.color == False:
            self.circle.setFill("white")

    def fake(self, win):
        self.circle.setFill('gray')
        self.draw(win)

    def disappear(self):
        self.circle.undraw()

    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)

    def draw(self, win):
        self.circle.draw(win)
    




        

    
