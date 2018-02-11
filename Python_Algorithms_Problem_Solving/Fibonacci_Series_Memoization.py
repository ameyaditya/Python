

def fibonaccci_ser(n):
    table = [-1]*(n+1)
    if(table[n] == -1):
        if n <= 1:
            table[n] = n
        else:
            table[n] = fibonaccci_ser(n-1) + fibonaccci_ser(n-2)
    return table[n]

number = input()
print(fibonaccci_ser(int(number)))
