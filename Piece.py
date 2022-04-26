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

    def fake(self, win):
        self.circle.setFill(color_rgb(198, 245, 232))
        self.draw(win)

    def disappear(self):
        self.circle.undraw()

    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)

    def draw(self, win):
        self.circle.draw(win)
    




        

    
