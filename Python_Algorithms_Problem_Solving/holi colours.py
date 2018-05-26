import numpy as np

# Write your code here
n,p,d,m = list(map(int,input().split()))
inp = [list(map(int,input().split())) for i in range(3)]
#inpu = list(map(int,inp))
inp = np.array(inp)
sum = 0
x = 3
while p>0 or d>0 or m>0:
    ind = inp.argmax()
    row = ind//x
    col = ind%x
    sum = sum + inp.max()
    '''
    for i in range(3):
        inp[i][col] = 0
        '''
    inp = np.delete(inp,col,1)
    if(row == 0):
        p = p-1
        x = x-1
    elif row == 1:
        d = d-1
        x = x-1
    else:
        m = m-1
        x = x -1
    a,b = inp.shape()
    if p == 0 and zip(a,b)!=0:
        '''
        for i in range(n):
            inp[0][i] = 0
        '''
        inp = np.delete(inp,row,0)
    if d == 0 and zip(a,b)!=0:
        '''
        for i in range(n):
            inp[1][i] = 0
        '''
        inp = np.delete(inp,row,0)
    if m == 0:
        '''
        for i in range(n):
            inp[2][i] = 0
        '''
        inp = np.delete(inp,row,0)
print(sum)
