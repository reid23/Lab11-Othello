#%%
from Board import Board

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
mat = []
for row in weightMatrix:
    mat += row

def mult(l):
    prod = 1
    for i in l:
        prod *= i
    return prod

def weights(board):
    return sum(map(mult, zip(mat, board.toVec())))


def analyze(board):

    nodes = [board.putCopy(mov) for mov in board.pMoves]

    if len(nodes) == 0: return False

    values = list(map(weights, nodes))

    # return dict(zip(board.pMoves, values))
    return max(values)
    # loop until move requested
    #   new list of current tree level {board: heuristic, board: heuristic, etc}
    #   start filling out heuristics based on last tree level list
    #
    # collapse tree, add up all of the heuristics, choose best one
    # collapse by adding up heuristics multiplied by inverse of layer, then highest is chosen
# heuristics:
#   total coins
#   weight matrix for locations
#   mobility
#   parity - stability
#%%
def calc(b, curDepth, maxDepth, player):
    if curDepth == maxDepth:
        return weights(b) + (b.score[player] - b.score[int(not player)])/2

    values = []
    for move in b.pMoves:
        values.append(calc(b.putCopy(move), curDepth+1, maxDepth, player))
    if len(values)==0:
        return 0

    if {'white': 1, 'black': 0}[b.player] == player:
        return max(values)
    return min(values)



#%%
b=Board()
ply = 2

# try:
while b.checkGameOver():
    moves = {}
    
    for move in b.pMoves:
        moves[move] = calc(b.putCopy(move), 0, ply, {'white': 1, 'black': 0}[b.player])
    
    try:
        b.put(max(moves, key = moves.get))
    except ValueError:
        print(f'no moves for {b.player}')
    print('moved')
print(b)
print(b.score)
# %%
