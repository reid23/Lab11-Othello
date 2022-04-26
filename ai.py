#%%
from Board import Board
from time import time
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
            mat += row

        def mult(self, l):
            return l[0]*l[1]


        def weights(self, board):
            return sum(map(self.mult, zip(self.mat, board.toVec())))



#%%
        # @profile
        def calc(self, b, curDepth, maxDepth, player):
            if curDepth == maxDepth:
                return self.weights(b) + (b.score[player] - b.score[int(not player)])/2 + len(b.pMovesVerbose) #pMovesVerbose is faster

            values = []
            for move in b.pMoves:
                values.append(calc(b.putCopy(move), curDepth+1, maxDepth, player))
            if len(values)==0:
                return 0

            if {'white': 1, 'black': 0}[b.player] == player:
                return max(values)
            return min(values)


        # @profile
        def __call__(self, b, player, depth = 5):

            start = time()
            moves = {}
            
            for move in b.pMoves:
                moves[move] = calc(b.putCopy(move), player, depth, {'white': 1, 'black': 0}[b.player])
            
            print(f'moved, took {time()-start}s')
            return max(moves, key = moves.get)


