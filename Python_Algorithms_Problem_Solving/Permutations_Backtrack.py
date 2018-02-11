def toString(a):
    return ''.join(a)
def permute(a,s,e):
    if s == e:
        print (toString(a), end=' ')
    else:
        for i in range(s,e+1):
            a[i],a[s] = a[s],a[i]
            permute(a,s+1,e)
            a[i],a[s] = a[s],a[i]
string = "ABCDE"
a = list(string)
length = len(string)
permute(a,0,length-1)
