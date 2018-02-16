
def print_solution(grid):
    for i in range(9):
        for j in range(9):
            print(grid[i][j],end=" ")
        print()
def is_solved(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return False
    return True
def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return [i,j]
def used_in_row(row,num,grid):
    for i in range(9):
        if num == grid[row][i]:
            return False
    return True

def used_in_col(col,num,grid):
    for i in range(9):
        if num == grid[i][col]:
            return False
    return True
def used_in_box(row,col,num,grid):
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col] == num:
                return False
    return True
def is_safe(row,col,num,grid):
    return used_in_row(row,num,grid) and used_in_col(col,num,grid) and used_in_box(row- row%3,col-col%3,num,grid)

def solve_sudoku(grid):
    #print_solution(grid)
    #input()
    #print()
    if is_solved(grid):
        print_solution(grid)
        return True
    row = find_empty(grid)[0]
    #print(row)
    col = find_empty(grid)[1]
    #print(col)
    for i in range(1,10):
        if is_safe(row,col,i,grid):
            grid[row][col] = i
            #print('inner')
            #print_solution(grid)
            #print()
            if(solve_sudoku(grid)):
                return True
            grid[row][col] = 0
    return False
grid2=[[0 for x in range(9)]for y in range(9)]
grid2=[[3,0,6,5,0,8,4,0,0],
      [5,2,0,0,0,0,0,0,0],
      [0,8,7,0,0,0,0,3,1],
      [0,0,3,0,1,0,0,8,0],
      [9,0,0,8,6,3,0,0,5],
      [0,5,0,0,9,0,6,0,0],
      [1,3,0,0,0,0,2,5,0],
      [0,0,0,0,0,0,0,7,4],
      [0,0,5,2,0,6,3,0,0]]
if solve_sudoku(grid2):
    print("yes")
else:
    print("no")
