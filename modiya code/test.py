nm = input().split()

n = int(nm[0])

m = int(nm[1])

a = list(map(int, input().rstrip().split()))

b = list(map(int, input().rstrip().split()))
a=sorted(a)
b=sorted(b)
c=[]
d=[]
for i in range (1,b[0]//a[0]+1):
    c.append(a[0]*i)
for j in range (1,len(a)) :
    for k in c :
        if k%a[j]!=0:
            d.append(k)
for j in range (len(b)):
    for k in c:
        print(k)
        if b[j]%k!=0:
            d.append(k)

c = set(c)
d = set(d)
print(len(c.difference(d)))
