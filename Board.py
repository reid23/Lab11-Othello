'''
Author: Reid

This file is a board class.  To get what you need to draw, do Board.getToDraw(). To make a move, use Board.put().
If there were no possible moves, but you still want to change whose turn it is, you can just call Board.switchTurn().  But Board.put() does this automatically.
'''
#%%
class Board:
    dirs =  [(-1, -1), (-1,  0), (-1,  1),
             ( 0, -1),           ( 0,  1),
             ( 1, -1), ( 1,  0), ( 1,  1)]

    def __init__(self, board: list = None):
        """constructor for board.  Initializes the board in starting position if `board` isn't passed.

        Args:
            board (list, optional): the board condition.  Do not pass, only used by the copy method. Defaults to None.
        """
        self.score = False
        #here's how the turn switchy thing works:
        # 0 represents black, 1 represents white, and 2 represents empty.
        # when the active player changes, _this and _other are swapped.  This way, the same code still works, and the values are just inverted (from the code's point of view).
        self._this =  0 #you are this, other is other
        self._other = 1
        self._empty = 2
                          # white
        self._colors = ["●", "◯", "-"] #for printing
                    #  black     empty
        if board!=None:
            self.board = board
            self.oldBoard = None
        else:
            self.board = [[self._empty for _ in range(8)] for _ in range(8)]
            self.oldBoard = Board(self.board) #init to all empty
            self.board[3][3] = self._this
            self.board[3][4] = self._other
            self.board[4][3] = self._other
            self.board[4][4] = self._this

        self._possibleMoves = {}
        self._calculatePossibleMoves()
        self._findEmptySquares = lambda x: self._empty in x
    
    def __str__(self):
        out = ""
        for row in self.board:
            for val in row:
                out += self._colors[val] + "  "
            out += "\n"
        return out[:-1]
    def __repr__(self):
        out = ""
        out += f"Board(board = [{self.board[0]}"
        for row in self.board[1:]:
            out += f"\n                {row}"
        out += f"], curColor = {self._colors})"
        return out
    def printWithMoves(self):
        for rowNum, row in enumerate(self.board):
            for colNum, val in enumerate(row):
                if (rowNum, colNum) in self.pMoves:
                    print(str(self.pMoves.index((rowNum, colNum))).center(2), end = " ")
                else:
                    print(self._colors[val], end = "  ")
            print()
    @property
    def player(self):
        return ['black', 'white'][self._this]

    def copy(self):
        """copies this board object.

        Returns:
            Board: another board object, identical to this one.
        """
        return Board(self.board)

    def put(self, pos: tuple):
        """places a piece at `pos`. The piece's color is the current turn.  This action toggles the turn.

        Args:
            pos (tuple): (r, c), where r and c are the coordinates of the position.
        """
        assert pos in self._possibleMoves.keys(), "Not a legal move"
        self._set(self._this, pos)
        self._flip(self._possibleMoves[pos])
        self.switchTurn()
        

    def putCopy(self, pos: tuple):
        """the same as Board.put, except it creates a copy and puts a piece in the copy.

        Args:
            pos (tuple): (r, c), where r and c are the coordinates of the position.
        """
        cp = self.copy()
        cp.put(pos)
        return cp

    def _flip(self, squares: tuple, curpos: tuple = (0, 0)):
        """flips the given squares.  Square location is relative to curpos, which defaults to (0,0) (aka absolute)
        Args:
            squares (tuple): the location of the squares to flip, relative to curpos.
            curpos (tuple, optional): the coordinates of the origin. Defaults to (0,0), meaning square locations are absolue.
        """
        if curpos!=(0,0):
            squares = map(sum, zip(squares, curpos)) #get absolute pos

        for square in squares:
            self.board[square[0]][square[1]] = int(not self.board[square[0]][square[1]])

    def _calculatePossibleMoves(self):
        """sets self._possibleMoves, based on the current game state.  Should be run at the start of every turn.
        """
        self._possibleMoves = {}
        for i in range(8):
            for j in range(8):
                legality = self._isLegal((i, j))
                if not not legality: self._possibleMoves[(i, j)] = legality
    @property
    def pMovesVerbose(self):
        """get the tiles flipped as well as the location of the movement

        Returns:
            dict: locations to move and tiles the flip, in the form {(r_1, c_1): [(pos), (pos)], etc.}
        """
        return self._possibleMoves

    @property
    def pMoves(self):
        """returns a tuple of tuples, representing the list of possible squares that the current player could choose.

        Returns:
            list: the possible locations to move, in the format [(r_1, c_1), (r_2, c_2), ... , (r_n, c_n)]
        """
        return list(self._possibleMoves.keys())
    
    def _get(self, pos: tuple):
        """gets the raw number at a position

        Args:
            pos (tuple): the position, (r, c)

        Returns:
            int: the value
        """
        return self.board[pos[0]][pos[1]]
    def _set(self, val: int, pos: tuple):
        """sets the square at `pos` to `val`

        Args:
            val (int): the value to enter
            pos (tuple): the position (c, r) to enter `val` at
        """
        self.board[pos[0]][pos[1]] = val
    def _findFlipsInDir(self, mov: tuple, dir: tuple):
        """checks whether pieces can be captured in a `dir`ection for `mov`

        Args:
            mov (tuple): the proposed movement location
            dir (tuple): the direction to check for flips in

        Returns:
            list: a list of the pieces to be flipped
        """
        toFlip = []
        curPos = list(mov)
        while True:
            curPos = list(map(sum, zip(curPos, dir)))
            try:
                piece = self._get(curPos)
            except IndexError:
                return []

            if piece == self._empty:
                return []

            if piece == self._this:
                if not toFlip:
                    return []
                return toFlip

            if piece == self._other:
                toFlip.append(curPos)
    def _isLegal(self, mov: tuple, curpos: tuple = (0,0)):
        """checks whether the given move (relative to curpos) is legal or not. Returns squares to flip if it is legal, to remove extra computation later.

        Args:
            mov (tuple): the proposed move, relative to curpos (which defaults to absolute position)
            curpos (tuple, optional): the current position. Defaults to (0,0), where mov will be an absolute movement.
        Returns:
            list | bool: a list of squares to flip, if legal, or False, if not legal.
        """
        toFlip = []
        if curpos!=(0,0): 
            mov = map(sum(map, zip(mov, curpos)))

        if self._get(mov) != self._empty: return False

        for dir in Board.dirs:
            toFlip+=self._findFlipsInDir(mov, dir)
        return toFlip if not not toFlip else False
    def switchTurn(self):
        """switches the turn.  this only needs to be run if there were no possible moves, so nothing was put in.
        This is also called by Board.put.  This is when Board._calculatePossibleMoves is run.
        """
        self.oldBoard = self.copy() #set last turn's board
        self._this, self._other = self._other, self._this
        self._calculatePossibleMoves()
        self.score = False
    def getToDraw(self):
        """returns which pieces should be drawn, and their locations.

        Returns:
            dict: the info about what should be drawn, in the format {'black': [(r, c), (r, c)...], 'white': [(r, c), (r, c)...], 'empty': [(r, c), (r, c), ...]}
        """
        return self - self.oldBoard
    @property
    def _boardList(self):
        """gets the raw board list. Only used by copy().

        Returns:
            list: the list describing the board
        """
        return self.board

    def __eq__(self, other):
        """checks if other is the same board as self.

        Args:
            other (any): The other thing to check for equality.

        Returns:
            bool: whether or not other is a board that is identical to this one.
        """
        try:
            return other.boardList==self.board
        except:
            raise NotImplementedError(f"Expected `other` of type Board, received {other.__class__.__name__}")
    def __sub__(self, other):
        """finds the difference between two boards, and returns the difference.  Add means thigns you should add to the other board to get this one (things that were added to this before the comparison)

        Args:
            other (Board): the other board, which this function will find the differences between

        Returns:
            dict: the difference, in the format {'black': [poses], 'white': [poses], 'empty': [poses]}
        """
        if not isinstance(other, Board): raise NotImplementedError(f"Expected `other` of type Board, received {other.__class__.__name__}")
        
        NAMES = ['black', 'white', 'empty']
        out = dict(zip(NAMES, [[],[],[],[]]))
        for i in range(8):
            for j in range(8):
                this = self._get((i, j))
                oth = other._get((i, j))
                if this==oth:
                    continue
                out[oth].append((i, j))
        return out
    def checkGameOver(self):
        """checks whether the game is over, currently just by checking if any squares are empty.

        Returns:
            bool: whether all squares are full
        """
        if True in map(self._findEmptySquares, self.board): #if there's no empty squares left, this is a shortcut to quickly catch this possibility. Not strictly needed.
            return True 
        if self.pMoves == (): #if current player's possible moves are empty
            cp = self.copy()
            cp.switchTurn()
            if cp.pMoves == (): #and next player's possible moves are empty
                return True  #then the game is over
        return False
    def getScore(self):
        if self.score: #if score has already been calculated for this game state, don't do it again
            return self.score
        self.score = (
            sum(list(map(lambda x: sum(list(map(lambda y: int(y==0), x))), self.board))), #find blacks
            sum(list(map(lambda x: sum(list(map(lambda y: int(y==1), x))), self.board))), #find whites
        )
        return self.score

if __name__ == '__main__':
    b=Board()
    while b.checkGameOver()==True:
        print("board:")
        b.printWithMoves()
        b.put(b.pMoves[int(input(f"{b.player.title()}, choose your move from {list(range(len(b.pMoves)))}: "))])
        print("\n\nnext turn!")
    score = b.getScore()
    if score[0]>score[1]:
        outcome = 'Black won.'
    elif score[0]<score[1]:
        outcome = 'White won.'
    else:
        outcome = 'Black and White tied.'
    print("Game over!", outcome)
    print(f"Final Score: {score}")