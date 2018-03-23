import sys
R = 3
C = 3
def min(x,y,z):
    if(x<y):
        return x if(x<z) else z
    else:
        return y if(y<z) else z
def mincost(cost,m,n):
    if(m<0 or n<0):
        return sys.maxsize
    elif(m == 0 and n == 0):
        return cost[m][n]
    else:
        return cost[m][n] + min(mincost(cost,m-1,n-1),mincost(cost,m,n-1),mincost(cost,m-1,n))

cost= [ [2, 2, 1],
        [1, 3, 1],
        [1, 1, 1] ]
print(mincost(cost,2,2))
