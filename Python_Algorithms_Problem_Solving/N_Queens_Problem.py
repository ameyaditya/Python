global N
N = 10


def printSol(board):
    for i in range(N):
        for j in range(N):
            print(board[i][j],end="  ")
        print()
def issafe(board,row,col):
    for x in range(col):
        if board[row][x] == 1:
            return False
    for x,y in zip(range(row,-1,-1),range(col,-1,-1)):
        if board[x][y] == 1:
            return False
    for x,y in zip(range(row,N,1),range(col,-1,-1)):
        if board[x][y] == 1:
            return False
    return True

def solveUntil(board,col):
    if col >= N:
        return True
    for i in range(N):
        if issafe(board,i,col):
            board[i][col] = 1
            if solveUntil(board,col+1) == True:
                return True
            board[i][col] = 0
    return False

def solve():
    board = [[0 for x in range(N)]for y in range(N)]
    if solveUntil(board,0) == False:
        print("the problem cannot be solved.")
        return False
    printSol(board)
    return True

solve()
