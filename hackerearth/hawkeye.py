
counter = 0
ans = []
for i in range(int(input())):
    counter = 0
    n,k = list(map(int,input().split()))
    m = list(map(int,input().split()))
    m.pop(0)
    x = k
    for j in range(1,n+1):
        x = x-1
        if x == 0:
            counter = counter + 1
            x = k
        elif j in m:
            counter = counter + 1
            x = k
    ans.append(counter)

for i in ans:
    print(i)
