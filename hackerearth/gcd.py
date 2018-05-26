from fractions import gcd
t = int(input())

ans =[]
for j in range(t):
    a,b,l,h = list(map(int,input().split()))
    flag = 0
    x = gcd(a,b)
    for i in range(h,l-1,-1):
        if x%i == 0:
            flag = 1
            print(i)
            break
    if flag == 0:
        print(-1)
