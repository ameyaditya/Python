import numpy as np
ans = []
for i in range(int(input())):
    n,m = list(map(int,input().split()))
    mat = [list(map(int,input().split())) for i in range(n)]
    abc = np.array(mat)
    if(n%2 == 1):
        ans.append(n)
    else:
        u = np.array(abc[:(n//2),:])
        l = np.array(abc[(n//2):,:])
        l = np.flip(l,0)
        while(np.array_equal(u,l) and n!=1):
            abc = u
            n = n//2
            u = np.array(abc[:(n//2),:])
            l = np.array(abc[(n//2):,:])
            l = np.flip(l,0)
        ans.append(n)
for i in ans:
    print(i)
