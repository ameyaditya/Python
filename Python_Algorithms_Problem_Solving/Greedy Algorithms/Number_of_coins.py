v = input()
v = int(v)
deno = [2000,500,200,100,50,20,10,5,2,1]
result = []

for item in deno:
    while v>= item:
        result.append(item)
        v = v-item

for res in result:
    print(str(res)+" ", end=" ")
