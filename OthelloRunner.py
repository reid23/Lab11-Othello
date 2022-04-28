# Hope Trygstad

from Board import Board
from GUIClass import GUI
from Piece import Piece
    

def main():
    board = Board()
    gui = GUI()
    pieces = gui.createPieces()
    while not gui.checkIfQuit():
        while not board.checkGameOver():
            board.getToDraw()
            moves = board.pMoves
            print(moves)
            print(board.getToDraw)
    

main()
    
