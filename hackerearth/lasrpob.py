n,m,q = list(map(int,input().split()))
dic = [[0]for i in range(n)]
for i in range(q):
    inp = list(map(int,input().split()))
    if(inp[0] == 0):
        dic[inp[1]].append(inp[3])
        dic[inp[2]].append(inp[3])
    elif inp[0] == 1:
        z = (set(dic[inp[1]]) & set(dic[inp[2]]))
        if(bool(z)):
            x = z.pop()
        if(x in dic[inp[1]]) and (x in dic[inp[2]]):
            dic[inp[1]].remove(x)
            dic[inp[2]].remove(x)
    else:
        print(max(dic[inp[1]]))
