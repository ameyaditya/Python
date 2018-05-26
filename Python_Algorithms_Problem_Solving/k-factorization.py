#!/bin/python3

import sys
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
while n > 1:
    if(i == len(A)-1):
        print(-1)
        flag = 1
        break
    k = n/A[i]
    if k in A or k==1:
        print("Entered if")
        ans.append(k)
        n = k
    else:
        print("Entered else")
        i +=1
ans.reverse()
if flag == 0:
    print(ans)
