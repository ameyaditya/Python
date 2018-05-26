from fractions import gcd
ans = []
for i in range(int(input())):
    ptr = 0
    a,b,l,h =list(map(int,input().split()))
    x = gcd(a,b)
    if x>=l and x<=h:
        ans.append(x)
    else:
        for j in range(x,1,-1):
            if(x%j == 0):
                if(j>=l and j<=h):
                    ans.append(j)
                    ptr = 1
                    break
        if ptr == 0:
            ans.append(-1)
for i in ans:
    print(i)
