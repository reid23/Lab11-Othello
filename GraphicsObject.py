# Hope Trygstad

class Piece:

    def __init__(self, color, x, y, win, GUI):
        self.color = color
        self.win = win
        self.x = x
        self.y = y
        self.gui = GUI
        self.color = color
        self.circle = Circle(Point(x, y))
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
    


   

        

    
