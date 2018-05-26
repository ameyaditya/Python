for i in range(int(input())):
    flag = 0
    a,b,l,h = list(map(int,input().split()))
    if((max(a,b)%min(a,b))== 0):
        print(max(a,b)//(min(a,b)))
    else:
        for i in range(l,h+1):
            if(a%i == 0) and (b%i == 0):
                print(i)
                flag = 1
                break
        if flag == 0:
            print(-1)
