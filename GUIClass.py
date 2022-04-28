# Hope Trygstad
# class for  Othello Game

#questions:
#   PLAYER CHOOSES IF THEY ARE WHITE OR BLACK- get to work in board
#   You should have some means of pointing out to the user what square the computer
#chose on its turn. Once either player has moved, your program should flip the
#appropriate discs to the correct color.


from graphics import *
from ButtonClass import Button
from Piece import Piece
from Board import Board
import math

class GUI:
    
    def __init__(self):
        self.win = GraphWin("Othello!!", 700, 800)
        self.win.setCoords(-1.5, 9.5, 8.5, -1.5)
        self.win.setBackground("grey")
        self.boardRect = Rectangle(Point(-0.5, -0.5), Point(7.5,7.5))
        self.boardRect.setFill("green")
        self.boardRect.draw(self.win)
        for i in range(8):
            horiz = Line(Point(-0.5, i-0.5), Point(7.5, i-0.5))
            horiz.draw(self.win)
            vert = Line(Point(i-0.5, 7.5), Point(i-0.5, -0.5))
            vert.draw(self.win)
            
                           
        self.messageBox = Rectangle(Point(-0.5, 7.75), Point(7.5, 9))
        self.messageBox.draw(self.win)
        self.quitButton = Button(self.win, Point(3.5,-1), 1.25, 0.4, "Click to Quit")
        self.quitButton.activate()
        self.message = Text(Point(3.5, 8.25), "Hi, Welcome to Othello!")
        self.message.setFill("white")
        self.message.draw(self.win)
        self.scoreText = Text(Point(3.5, 8.75), "Black: 0     White: 0")
        self.scoreText.setFill("white")
        self.scoreText.draw(self.win)

        numsList = ["1","2","3","4","5","6","7","8"]
        letters = ["a","b","c","d","e","f","g", "h"]
        for i in range(8):
            num = Text(Point(i, -0.65), numsList[i])
            num.setFill("white")
            num.draw(self.win)
            let = Text(Point(-0.7, i), letters[i])
            let.setFill("white")
            let.draw(self.win)

    def getTeam(self):
        self.miniwin = GraphWin("Choose your team!", 200, 200)
        teamText = Text(Point(100, 50), "Chose your team! Black goes first.")
        teamText.draw(self.miniwin)
        whiteButton = Button(self.miniwin, Point(50, 125), 50, 25, "White")
        blackButton = Button(self.miniwin, Point(150, 125), 50, 25, "Black")
        whiteButton.activate()
        blackButton.activate()
        p = self.miniwin.getMouse()
        if whiteButton.clicked(p):
            team = "w"
        if blackButton.clicked(p):
            team = "b"
        self.miniwin.close()
        return team
        
    def createPieces(self):
        "Sets up the initial pieces on the board"
        piecesList = [
            Piece(True, 3, 3),
            Piece(True, 4,4),
            Piece(False, 3, 4),
            Piece(False, 4, 3),
        ]
        for i in piecesList:
            i.draw(self.win)
        return piecesList

    def getWin(self):
        return self.win

##    def getMouse(self):
##        self.win.getMouse()

    def changeMessage(self, text):
        self.message.undraw()
        self.message.setText(text)
        self.message.draw(self.win)

    def blackTurn(self):
        self.changeMessage("Black, choose your move from the illuminated \
squares.")

    def whiteTurn(self):
        self.changeMessage("White, choose your move from the illuminated \
squres.")

    def updateScore(self, board):
        score = board.score
        print("raw score: ", board.score)
        newScore = "Black: " + str(score[0]) + " White: " + str(score[1])
        self.scoreText.setText(newScore)

    def invalidMove(self):
        self.changeMessage("Sorry, that move was invalid. Please pick again!")

    def noMoves(self):
        self.changeMessage("No valid moves. Click anywhere to continue game.")

    def drawPiece(self, piece, x, y):
        "Draws an object onto the board, with the thing and its coordinates \
        as parameters"
        piece.draw(self.win)

    def checkIfQuit(self):
        p = self.win.getMouse()
        if self.quitButton.clicked(p):
            return True
        else: return False

    def mouseClick(self):
        "Shows the user all legal squares, lets them choose their move, \
        does the move in the board, then animates that the AI did in \
        response"
        p = self.win.getMouse()
        return p

    def __animate_AI(self):
        "shows the user what move the AI did"
        pass

    def showAllowedMoves(self, on, turn, moves, win):
        if on == True:
            circles = []
            for i in moves:
                circles.append(Piece(turn, i[0], i[1]))
            for circle in circles:
                circle.fake(self.win)
        return circles

    def gameOver(self, b):
        score = b.score
        if score[0]>score[1]:
            outcome = 'Black won.'
        elif score[0]<score[1]:
            outcome = 'White won.'
        else:
            outcome = 'Black and White tied.'
        outOutcome = "Game over!", outcome
        self.changeMessage(outOutcome)
        print(f"Final Score: {score}")


def main():
    gui = GUI()
    team = gui.getTeam()
    b = Board()
    pieces = gui.createPieces()
    print("current pieces: ", pieces)

    if team == "b":
        turn = True
    else:
        turn = False
    moves = b.pMoves


    while not b.checkGameOver():
        if turn == True:
            gui.blackTurn()
        else:
            gui.whiteTurn()
        
        print("possible moves: ", moves)
        fakeCircles = gui.showAllowedMoves(True, turn, moves, gui.getWin())

        if len(moves) == 0:
            gui.noMoves()
            continue

        p = gui.mouseClick()
        if gui.quitButton.clicked(p):
            gui.win.close()
            return
            break
        xmove = round(p.getX())
        ymove = round(p.getY())
        theMove = (ymove, xmove)
        print("the move is ", theMove)
        
        while theMove not in moves:
            gui.invalidMove()
            p = gui.mouseClick()
            if gui.quitButton.clicked(p):
                gui.win.close()
                return
                break
            xmove = round(p.getX())
            ymove = round(p.getY())
            theMove = (ymove, xmove)
        b.put(theMove)
        a = b.getToDraw()
        print("get to draw is ", a)
        x = a.get('black')
        for i in x:
            newPiece = Piece(True, i[0], i[1])
            gui.drawPiece(newPiece, i[0], i[1])
        y = a.get('white')
        for i in y:
            newPiece = Piece(False, i[0], i[1])
            gui.drawPiece(newPiece, i[0], i[1])

        for i in fakeCircles:
            i.disappear()
        if turn == True:
            turn = False
        else:
            turn = True
        gui.updateScore(b)
        moves = b.pMoves

    gui.gameOver(b)

if __name__ == '__main__': main()
    

