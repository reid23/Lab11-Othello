# Hope Trygstad
# class for graphics objects in the Othello Game

class GUI:
    def __init__(self):
        self.win = GraphWin("Othello", 800, 800)
        self.win.setCoords(-1.5, -1.5, 8.5, 8.5)
        self.win.setBackground("grey")
        self.image = Image(Point(
        self.messageBox = Rectangle(Point(0
        self.quitButton = Button(self.win, Point(,), 2, 1, "Click to Quit")
        self.quitButton.activate()
        self.playAgain = Button(self.win, Point(,), 2, 1, "Play Again")

    def createPieces(self):
        "Sets up the initial pieces on the board"

    
        
        
    
