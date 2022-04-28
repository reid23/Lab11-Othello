'''
Author: Reid Dye

Not that I'm particularly proud of that; this is probably the worst code I've ever written, but hey, it works!
This file is something I threw together quickly as a backup plan in case the actual file didn't get finished.
'''


from graphics import *
from ButtonClass import Button
from Piece import Piece
from Board import Board
from ai import ai

def gui():

    #win and background and coords
    global win
    win = GraphWin("Othello!!", 700, 800)
    win.setCoords(-1.5, 9.5, 8.5, -1.5)
    win.setBackground("grey")

    #board background
    boardRect = Rectangle(Point(-0.5, -0.5), Point(7.5,7.5))
    boardRect.setFill("green")
    boardRect.draw(win)

    #lines for squares
    for i in range(8):
        horiz = Line(Point(-0.5, i-0.5), Point(7.5, i-0.5))
        horiz.draw(win)
        vert = Line(Point(i-0.5, 7.5), Point(i-0.5, -0.5))
        vert.draw(win)
        
    #message box, quit button, message, and score
    global messageBox
    messageBox = Rectangle(Point(-0.5, 7.75), Point(7.5, 9))
    messageBox.draw(win)
    global quitButton
    quitButton = Button(win, Point(3.5,-1), 1.25, 0.4, "Click to Quit")
    quitButton.activate()
    global message
    message = Text(Point(3.5, 8.25), "Hi, Welcome to Othello!")
    message.setFill("white")
    message.draw(win)
    global scoreText
    scoreText = Text(Point(3.5, 8.75), "Black: 0     White: 0")
    scoreText.setFill("white")
    scoreText.draw(win)

    global lastMoveMarker
    lastMoveMarker = Circle(Point(0,0), 0.15)
    lastMoveMarker.setFill('gray')


    #row, col labels
    for i in range(8):
        num = Text(Point(i, -0.65), str(i+1))
        num.setFill("white")
        num.draw(win)
        let = Text(Point(-0.7, i), chr(i+97))
        let.setFill("white")
        let.draw(win)


def getTeam():
    miniwin = GraphWin("Choose your team!", 200, 200)
    teamText = Text(Point(100, 50), "Chose your team! Black goes first.")
    teamText.draw(miniwin)
    whiteButton = Button(miniwin, Point(50, 125), 50, 25, "White")
    blackButton = Button(miniwin, Point(150, 125), 50, 25, "Black")
    whiteButton.activate()
    blackButton.activate()
    p = miniwin.getMouse()
    if whiteButton.clicked(p):
        team = "w"
    if blackButton.clicked(p):
        team = "b"
    miniwin.close()
    return team
        


def draw(poses, win):
    for pos in poses['black']:
        Piece(True, *pos).draw(win)
    for pos in poses['white']:
        Piece(False, *pos).draw(win)
    


def getDesiredMove(b):
    global message
    message.setText(f'{b.player.title()}, choose your move from the shown squares.')

    while True:
        click = win.getMouse()
        if quitButton.clicked(click):
            win.close()
            return
        selMove = tuple(map(round, (click.getY(), click.getX())))

        if selMove in b.pMoves and 0<=selMove[0]<=7 and 0<=selMove[1]<=7:
            break
        message.setText("Sorry, that move was invalid. Please pick again!")
    return selMove


def updateLastMoveMarker(move):
    global lastMoveMarker
    lastMoveMarker.undraw()
    curPos = (lastMoveMarker.getCenter().getY(), lastMoveMarker.getCenter().getX())
    lastMoveMarker.move(move[1]-curPos[1], move[0]-curPos[0])
    lastMoveMarker.draw(win)

def main():
    gui()

    global win
    global message
    global scoreText
    global lastMoveMarker

    b = Board()
    aiPlayer = ai()
    
    draw(b.getToDraw(), win)
    

    if getTeam() == 'b':

        possibleMoveMarkers = [Piece(True, *pos) for pos in b.pMoves]
        for marker in possibleMoveMarkers:
            marker.fake(win)
        
        selMove = getDesiredMove(b)
        b.put(selMove)
        for marker in possibleMoveMarkers:
            marker.disappear()
        
        draw(b.getToDraw(), win)
        updateLastMoveMarker(selMove)
        scoreText.setText(f'Black: {b.score[0]}, White: {b.score[1]}')
    
    while not b.checkGameOver():
        #ai turn
        message.setText(f'{b.player} (AI) is selecting their move...')

        possibleMoveMarkers = [Piece(True, *pos) for pos in b.pMoves]
        for marker in possibleMoveMarkers:
            marker.fake(win)
        
        aiMove = aiPlayer(b, 4)

        if len(aiMove)>0:
            b.put(aiMove)
            draw(b.getToDraw(), win)
            updateLastMoveMarker(aiMove)
            scoreText.setText(f'Black: {b.score[0]}, White: {b.score[1]}')
        else:
            b.put(())
        for marker in possibleMoveMarkers:
            marker.disappear()



        #human turn
        if len(b.pMoves)>0:

            possibleMoveMarkers = [Piece(True, *pos) for pos in b.pMoves]
            for marker in possibleMoveMarkers:
                marker.fake(win)
            
            selMove = getDesiredMove(b)
            b.put(selMove)

            for marker in possibleMoveMarkers:
                marker.disappear()

            draw(b.getToDraw(), win)
            updateLastMoveMarker(selMove)
        else:
            b.put(())

        scoreText.setText(f'Black: {b.score[0]}, White: {b.score[1]}')
    outcome = ''
    if b.score[0]>b.score[1]:
        outcome = 'Black won!'
    if b.score[1]<b.score[0]:
        outcome = 'White won!'
    if b.score[0]==b.score[1]:
        outcome = 'Black and White tied!'
    message.setText(f'Game over! {outcome}')

    win.getMouse()
    



if __name__ == '__main__': main()
    

