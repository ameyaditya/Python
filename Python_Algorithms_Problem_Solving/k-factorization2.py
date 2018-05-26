n, k = input().strip().split(' ')
n = int(n)
k = int(k)
A = list(map(int, input().strip().split(' ')))
A = sorted(A,reverse=True)
k = 100
i = 0
flag = 0
ans = []
ans.append(n)
while k>1:
    if(i == len(A)-1):
        print(-1)
        flag = 1
        break
    k = n/A[i]
    m = n%A[i]
    if m == 0:
        n = k
        if k!=1:
            ans.append(k)
        i +=1
    else:
        i +=1
if flag == 0:
    ans.append(1)
    ans.reverse()
    for i in ans:
        print(int(i),end=" ")
