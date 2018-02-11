import sys
global N
N = 5
def printSol(sol):
    for i in range(N):
        for j in range(N):
            print(sol[i][j],end=" ")
        print()
def issafe(maze,x,y):
    if x>=0 and x<N and y>=0 and y<N and maze[x][y] == 1:
        return True
    return False
def solve_maze(maze,x,y,sol,d):
    if x== N-1 and y == N-1:
        sol[x][y] = 1
        return True
    if issafe(maze,x,y):
        sol[x][y] = 1
        if d!='u' and solve_maze(maze,x+1,y,sol,'d') == True:
            return True
        if d!='l' and solve_maze(maze,x,y+1,sol,'r') == True:
            return True
        if d!='d' and solve_maze(maze,x-1,y,sol,'u') == True:
            return True
        if d!='r' and solve_maze(maze,x,y-1,sol,'l') == True:
            return True
        sol[x][y] = 0
    return False

def solve(maze):
    sol = [[0 for x in range(N)]for y in range(N)]
    res = solve_maze(maze,0,0,sol,'d')
    if res == False:
        print("Cannot be solved")
        return False
    printSol(maze)
    print()
    printSol(sol)
    return True
maze =[ [ 1, 0, 1, 1, 1 ],
        [ 1, 1, 1, 1, 1 ],
        [ 0, 1, 0, 1, 1 ],
        [ 0, 1, 1, 1, 0 ],
        [ 0, 0, 0, 1, 1 ] ]
solve(maze)
