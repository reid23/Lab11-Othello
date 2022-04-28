'''
Author: Reid Dye

This file contains the ai class, and runs an ai vs. ai game when run.
If it looks sketchy or has questionable design choices, it's because i wrote this too quickly and without planning enough.
It started as all just functions to do simple induvidual things, and once that worked, I made it into a full class.
'''

#%%
# from Board import Board
from time import time
from functools import lru_cache
import math
class ai:
    def __init__(self):
        """constructor for an AI.  just creates the weight matrix
        """
        weightMatrix = [
            [4,-3,2,2,2,2,-3,4],
            [-3,-4,-1,-1,-1,-1,-4,-3],
            [2,-1,1,0,0,1,-1,2],
            [2,-1,0,1,1,0,-1,2],
            [2,-1,0,1,1,0,-1,2],
            [2,-1,1,0,0,1,-1,2],
            [-3,-4,-1,-1,-1,-1,-4,-3],
            [4,-3,2,2,2,2,-3,4],
        ]
        self.mat = []
        for row in weightMatrix:
            self.mat += row #make into vector

    # @lru_cache(None)
    def _weights(self, board): #returns how good it is for white
        return sum(map(math.prod, zip(self.mat, board.toVec()))) #dot product of the weights and the board

    def _heuristic(self, board): #evaluates the favorability of a board, FOR WHITE
            weights = self._weights(board)*board.playerNum #how good it is for white
            out = weights*1.8 \
                + (board.score[1] - board.score[0]) \
                + board.playerNum*(len(board.pMovesVerbose)) #pMovesVerbose is faster
            return out
    # @lru_cache(None)
    def _calc(self, b, curDepth, maxDepth, player): #recursive search algorithm
        if curDepth == maxDepth:
            return self._heuristic(b) #base case

        values = []
        for move in b.pMoves:
            values.append(self._calc(b.putCopy(move), curDepth+1, maxDepth, player)) #look for best move
        if len(values)==0:
            return 0

        if b.playerNum == (2*player)-1: #if we're playing, 
            return self._heuristic(b.putCopy(b.pMoves[values.index(max(values))])) #return the best move for us
        else: 
            return self._heuristic(b.putCopy(b.pMoves[values.index(min(values))])) #else return the worst move for us


    
    def __call__(self, b, depth = 4): #this is how you actually get a result

        start = time()
        moves = {}
        
        for move in b.pMoves:
            moves[move] = self._calc(b.putCopy(move), 0, depth, (b.playerNum+1)/2)
        
        print(f'moved, took {repr(time()-start)}s')
        try:
            return max(moves, key = moves.get)
        except ValueError:
            return ()

if __name__ == '__main__':
    from Board import Board
    board=Board()
    a=ai()
    while not board.checkGameOver():
        board.put(a(board))
        board.put(a(board))
    print(board)
    print(board.score)


