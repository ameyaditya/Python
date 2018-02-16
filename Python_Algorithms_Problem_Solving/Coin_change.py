def coinchange(s,m,n):
    table = [0 for i in range(n+1)]
    table[0] = 1

    for i in range(0,m):
        for j in range(s[i],n+1):
            table[j]+=table[j-s[i]]
    return table[n]

arr = [1, 2, 3]
m = len(arr)
n = 4
x = coinchange(arr, m, n)
print (x)
