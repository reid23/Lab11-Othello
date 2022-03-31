# Hope Trygstad

from graphics import *
from GUIClass import GUI

class Piece:

    def __init__(self, color, x, y, GUI):
        self.color = color
        self.x = x
        self.y = y
        self.gui = GUI
        self.win = self.gui.getWin()
        self.color = color
        self.circle = Circle(Point(x, y), 0.35)
        if self.color == True:
            self.circle.setFill("black")
        if self.color == False:
            self.circle.setFill("white")
        self.circle.draw(self.win)


    def getX(self):
        return(self.x)

    def getY(self):
        return(self.y)

    def draw(self):
        "draws the piece into the GUI, showing a color change if their \
        was one"
        if self.color == True:
            self.circle.setFill("black")
        if self.color == False:
            self.circle.setFill("white")
        # this is confusing me
        #self.gui.drawThing(

    def __flip(self):
        "Changes the color of the piece. No parameters since it can only change\
        one way"
        if self.color == True:
            self.color = False
        else:
            self.color = True
    


def main():
    myGUI = GUI()
    piece1 = Piece(True, 3, 4, myGUI)

main()

        

    
