class Board:
    def __init__(self, board: list = None):
        """constructor for board.  Initializes the board in starting position if `board` isn't passed.

        Args:
            board (list, optional): the board condition.  Do not pass, only used by the copy method. Defaults to None.
        """
        pass
    def copy(self):
        """copies this board object.

        Returns:
            Board: another board object, identical to this one.
        """
        pass

    def put(self, pos: tuple):
        """places a piece at `pos`.  the piece's color is the current turn.  This action toggles the turn.

        Args:
            pos (tuple): (x, y), where x and y are the coordinates of the position.
        """
        pass

    def putCopy(self, pos: tuple):
        """the same as Board.put, except it creates a copy and puts a piece in the copy.

        Args:
            pos (tuple): (x, y), where x and y are the coordinates of the position.
        """
        pass
    def _flip(self, squares: tuple, curpos: tuple = (0, 0)):
        """flips the given squares.  Square location is relative to curpos, which defaults to (0,0) (aka absolute)
        Args:
            squares (tuple): the location of the squares to flip, relative to curpos.
            curpos (tuple, optional): the coordinates of the origin. Defaults to (0,0), meaning square locations are absolue.
        """
        pass

    def _calculatePossibleMoves(self):
        """sets self.possibleMoves, based on the current game state.  Should be run at the start of every turn.
        """

    @property
    def possibleMoves(self):
        """returns a tuple of tuples, representing the list of possible squares that the current player could choose.

        Returns:
            tuple: the possible locations to move, in the format ((x_1, y_1), (x_2, y_2), ... , (x_n, y_n))
        """
        pass
    def isLegal(self, mov: tuple, curpos: tuple = (0,0)):
        """checks whether the given move (relative to curpos) is legal or not.

        Args:
            mov (tuple): the proposed move, relative to curpos (which defaults to absolute position)
            curpos (tuple, optional): the current position. Defaults to (0,0), where mov will be an absolute movement.
        """
        pass
    def switchTurn(self):
        """switches the turn.  this only needs to be run if there were no possible moves, so nothing was put in.
        This is also called by Board.put.  This is when Board._calculatePossibleMoves is run.
        """
        pass
    def getToDraw(self):
        """returns which pieces should be drawn, and their locations.

        Returns:
            dict: the info about what should be drawn, in the format {'black': ((x,y), (x,y)...), 'white': ((x,y), (x,y)....)}
        """