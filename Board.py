'''
Author: Reid

This file is a board class.  To get what you need to draw, do Board.getToDraw(). To make a move, use Board.put().
If there were no possible moves, but you still want to change whose turn it is, you can just call Board.switchTurn().  But Board.put() does this automatically.
'''
#%%
class Board:
    MOVES = [
                (-1, -1),
                (-1,  0),
                (-1,  1),
                ( 0, -1),
                ( 0,  1),
                ( 1, -1),
                ( 1,  0),
                ( 1,  1),
            ]

    def __init__(self, board: 'list[list[int]]' = None):
        """constructor for board.  Initializes the board in starting position if `board` isn't passed.

        Args:
            board (list, optional): the board condition.  Do not pass, only used by the copy method. Defaults to None.
        """
        self._score = False
        #here's how the turn switchy thing works:
        # 0 represents black, 1 represents white, and 2 represents empty.
        # when the active player changes, _this and _other are swapped.  This way, the same code still works, and the values are just inverted (from the code's point of view).
        self._this =  0 #you are this, other is other
        self._other = 1
        self._empty = 2
                          # white
        self._colors = ["●", "◯", "-"] #for printing
                    #  black     empty
        if board != None:
            self._board = board
            self.oldBoard = None
        else:
            self._board = [[self._empty for _ in range(8)] for _ in range(8)]
            self.oldBoard = Board(self._board) #init to all empty
            self._set(self._this,  (3, 3))
            self._set(self._other, (3, 4))
            self._set(self._other, (4, 3))
            self._set(self._this,  (4, 4))

        self._possibleMoves = {}
        self._calculatePossibleMoves()
        self._findEmptySquares = lambda x: self._empty in x
    
    def __str__(self) -> str:
        """human-readable string representation of this board. used by str(board), print(), etc.

        Returns:
            str: the string
        """
        out = ""
        for row in self._board:
            for val in row:
                out += self._colors[val] + "  "
            out += "\n"
        return out[:-1]
    def __repr__(self) -> str:
        """exact string representation of the constructor needed to make a copy of this object.

        Returns:
            str: the string
        """
        out = ""
        out += f"Board(board = [{self._board[0]}"
        for row in self._board[1:]:
            out += f"\n                {row}"
        out += f"], curColor = {self._colors})"
        return out
    def printWithMoves(self) -> None:
        """prints out the current game, with unique numers in each of the possible moves, so the user can see where they want to move.
        """
        for rowNum, row in enumerate(self._board):
            for colNum, val in enumerate(row):
                if (rowNum, colNum) in self.pMoves:
                    print(str(self.pMoves.index((rowNum, colNum))).center(2), end = " ")
                else:
                    print(self._colors[val], end = "  ")
            print()
    @property
    def player(self) -> str:
        """the current active player

        Returns:
            str: the player, either 'black' or 'white'
        """
        return ['black', 'white'][self._this]

    def copy(self):
        """copies this board object.

        Returns:
            Board: another board object, identical to this one.
        """
        return Board(list(map(list.copy, self._board))) #deep copy, slower but neccessary

    def put(self, pos: 'tuple[int]') -> None:
        """places a piece at `pos`. The piece's color is the current turn. This action toggles the turn. If pos is an empty tuple, no piece is placed, but the turn is still switched.

        Args:
            pos (tuple): (r, c), where r and c are the coordinates of the position. If an empty tuple is passed, nothing will be placed, and the turn will be switched.
        """
        if pos == () == tuple(self.pMoves): #if nothing is passed, and there are no legal moves (ie player is allowed to not make a move), just switch the turn.
            self._switchTurn()
            return
        assert pos in self.pMoves, "Not a legal move.  Expected move in {self.pMoves} but received {pos}."
        self.oldBoard = self.copy()
        self._set(self._this, pos)
        self._flip(self._possibleMoves[pos])
        self._switchTurn()
        
    def putCopy(self, pos: 'tuple[int]'):
        """the same as Board.put, except it creates a copy and puts a piece in the copy.

        Args:
            pos (tuple): (r, c), where r and c are the coordinates of the position.

        Returns:
            Board: the copied board with the new piece
        """
        cp = self.copy()
        cp.put(pos)
        return cp

    def _flip(self, squares: 'tuple[tuple[int]]', curpos: 'tuple[int]' = (0, 0)) -> None:
        """flips the given squares.  Square location is relative to curpos, which defaults to (0,0) (aka absolute)

        Args:
            squares (tuple): the location of the squares to flip, relative to curpos.
            curpos (tuple, optional): the coordinates of the origin. Defaults to (0,0), meaning square locations are absolue.
        """
        if curpos!=(0,0):
            squares = (squares[0]+curpos[0], squares[1]+curpos[1]) #get absolute pos

        for square in squares:
            self._set(int(not self._get(square)), square)
    # @profile
    def _calculatePossibleMoves(self) -> None:
        """sets self._possibleMoves, based on the current game state. runs at the start of every turn.
        """
        self._possibleMoves = {}
        for i in range(8):
            for j in range(8):
                legality = self._isLegal((i, j))
                if not not legality: self._possibleMoves[(i, j)] = legality
    @property
    def pMovesVerbose(self) -> 'dict[tuple[int]: list[tuple[int]]]':
        """get the tiles flipped along with each possible move

        Returns:
            dict: locations to move and tiles that flip, in the form {(mov_row, mov_col): [(flip_row, flip_col), (flip_row, flip_col)], etc.}
        """
        return self._possibleMoves

    @property
    def pMoves(self) -> 'list[tuple[int]]':
        """returns a list of tuples, representing the list of possible squares that the current player could choose.

        Returns:
            list: the possible locations to move, in the format [(r_1, c_1), (r_2, c_2), ... , (r_n, c_n)]
        """
        return list(self._possibleMoves.keys())
    
    def _get(self, pos: 'tuple[int]') -> int:
        """gets the raw number at a position

        Args:
            pos (tuple): the position, (r, c)

        Returns:
            int: the value
        """
        r, c = pos
        return self._board[r][c] if (0<=r<=7 and 0<=c<=7) else -1
    def _set(self, val: int, pos: 'tuple[int]') -> None:
        """sets the square at `pos` to `val`

        Args:
            val (int): the value to enter
            pos (tuple): the position (c, r) to enter `val` at
        """
        self._board[pos[0]][pos[1]] = val
    
    # @jit
    # @profile
    def _findFlipsInDir(self, mov: 'tuple[int]', dir: 'tuple[int]') -> 'list[tuple[int]]':
        """checks whether pieces can be captured in a `dir`ection for `mov`

        Args:
            mov (tuple): the proposed movement location
            dir (tuple): the direction to check for flips in

        Returns:
            list: a list of the pieces to be flipped
        """
        toFlip = []
        mov = list(mov)
        
        while True:
            mov = [mov[0]+dir[0], mov[1]+dir[1]]

            piece = self._get(mov) #get the piece
            if piece == self._empty or piece == -1: #when mov is out of bounds or there's no piece at this square
                return []
            if piece == self._this: #if it's the same color, there's a bracket!  if there's no space between the two sides, though, it'll still just return an empty list.
                return toFlip
            if piece == self._other:
                toFlip.append(mov)
    # @jit
    # @profile
    def _isLegal(self, mov: 'tuple[int]', curpos: 'tuple[int]' = (0,0)) -> 'list[tuple[int]]':
        """checks whether the given move (relative to curpos) is legal or not. Returns squares to flip if it is legal, to remove extra computation later.

        Args:
            mov (tuple): the proposed move, relative to curpos (which defaults to absolute position)
            curpos (tuple, optional): the current position. Defaults to (0,0), where mov will be an absolute movement.
        Returns:
            list: a list of squares to flip. An empty list means the move is illegal.
        """
        toFlip = []
        if curpos!=(0,0): 
            mov = (mov[0]+curpos[0], mov[1]+curpos[1])

        if self._get(mov) != self._empty: return False

        for dir in Board.MOVES:
            toFlip+=self._findFlipsInDir(mov, dir)
        return toFlip
    def _switchTurn(self) -> None:
        """switches the turn.  this only needs to be run if there were no possible moves, so nothing was put in.
        This is also called by Board.put.  This is when Board._calculatePossibleMoves is run.
        """
        self._this, self._other = self._other, self._this
        self._calculatePossibleMoves()
        self._score = False
    def getToDraw(self) -> 'dict[str: list[tuple[int]]]':
        """returns which pieces should be drawn, and their locations.

        Returns:
            dict: the info about what should be drawn, in the format {'black': [(r, c), (r, c)...], 'white': [(r, c), (r, c)...], 'empty': [(r, c), (r, c), ...]}
        """
        return self.oldBoard - self #uses __sub__

    def __eq__(self, other) -> bool:
        """checks if other is the same board as self.

        Args:
            other (Board): The other thing to check for equality.

        Returns:
            bool: whether or not other is a board that is identical to this one.
        """
        try:
            return other.board==self._board
        except:
            raise NotImplementedError(f"Expected `other` of type Board, received {other.__class__.__name__}")
    def __sub__(self, other) -> 'dict[str: list[tuple[int]]]':
        """finds the difference between two boards, and returns the difference. to use, do old_board - new_board.  It will return a dict of things to set to make changes.

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
                out[NAMES[oth]].append((i, j))
        return out
    def checkGameOver(self) -> bool:
        """checks whether the game is over.

        Returns:
            bool: whether all squares are full
        """
        if True in map(self._findEmptySquares, self._board): #if there's no empty squares left, this is a shortcut to quickly catch this possibility. Not strictly needed.
            return True 
        if self.pMoves == (): #if current player's possible moves are empty
            cp = self.copy()
            cp._switchTurn()
            if cp.pMoves == (): #and next player's possible moves are empty
                return True  #then the game is over
        return False
    
    @property
    def score(self) -> 'tuple[int]':
        """the current score

        Returns:
            tuple: the score, in the form (black tiles, white tiles)
        """
        if self._score: #if score has already been calculated for this game state, don't do it again
            return self._score
        self._score = (
            sum(list(map(lambda x: sum(list(map(lambda y: int(y==0), x))), self._board))), #find blacks
            sum(list(map(lambda x: sum(list(map(lambda y: int(y==1), x))), self._board))), #find whites
        )
        return self._score
#%%
def main():
    b=Board()
    while b.checkGameOver()==True:
        print("board:")
        b.printWithMoves()
        b.put(b.pMoves[int(input(f"{b.player.title()}, choose your move from {list(range(len(b.pMoves)))}: "))])
        print(b.getToDraw())
        print("\n\nnext turn!")
    score = b.score()
    if score[0]>score[1]:
        outcome = 'Black won.'
    elif score[0]<score[1]:
        outcome = 'White won.'
    else:
        outcome = 'Black and White tied.'
    print("Game over!", outcome)
    print(f"Final Score: {score}")


if __name__ == '__main__':
    b=Board()
    from timeit import timeit as t
    from time import sleep
    sleep(2)
    print(t('b._calculatePossibleMoves()', number = 10000, globals = globals()))
    # try:
    #     main()
    # except KeyboardInterrupt:
    #     print("\nExiting.")
# %%
