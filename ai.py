#%%
from Board import Board
from time import time
from functools import lru_cache
import math
class ai:
    def __init__(self):
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
            self.mat += row


    def mult(self, l):
        return l[0]*l[1]

    # @lru_cache(None)
    def weights(self, board):
        return sum(map(math.prod, zip(self.mat, board.toVec())))

    def calc(self, b, curDepth, maxDepth, player):
        if curDepth == maxDepth:
            if player==1:
                weights = self.weights(b)
            else:
                weights = -1*self.weights(b)
            return weights + (b.score[player] - b.score[int(not player)])/2 + len(b.pMovesVerbose)/2 #pMovesVerbose is faster

        values = []
        for move in b.pMoves:
            values.append(self.calc(b.putCopy(move), curDepth+1, maxDepth, player))
        if len(values)==0:
            return 0

        if {'white': 1, 'black': 0}[b.player] == player: #if we're playing, 
            return max(values) #return the best move for us
        return min(values) #else return the worst move for us


    
    def __call__(self, b, depth = 3):

        start = time()
        moves = {}
        
        for move in b.pMoves:
            moves[move] = self.calc(b.putCopy(move), 0, depth, {'white': 1, 'black': 0}[b.player])
        
        print(f'moved, took {time()-start}s')
        try:
            return max(moves, key = moves.get)
        except ValueError:
            return ()

if __name__ == '__main__':
    b=Board()
    a=ai()
    while not b.checkGameOver():
        b.put(a(b))
        b.put(a(b))
    print(b)
    print(b.score)


