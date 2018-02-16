R = 3
C = 3
def mincost(cost,x,y):
    tc = [[0 for i in range(C)]for j in range(R)]
    tc[0][0] = cost[0][0]

    for i in range(1,x+1):
        tc[i][0] = tc[i][x-1] + cost[i][0]
    for i in range(1,y+1):
        tc[0][i] = tc[y-1][i] + cost[i][0]
    for i in range(1,x+1):
        for j in range(1,y+1):
            tc[i][j] = cost[i][j] + min(tc[i-1][j-1],tc[i-1][j],tc[i][j-1])
    print(tc[x][y])
def min(x,y,z):
    if(x<y):
        return x if(x<z) else z
    else:
        return y if(y<z) else z

cost= [ [1, 2, 3],
        [4, 1, 2],
        [1, 5, 3] ]
print(mincost(cost,2,2))
