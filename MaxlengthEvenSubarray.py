for i in range(int(input())):
    n = int(input())
    
    x = int(n/2)
    if(n/2 > x): x = x + 1
    
    if(x % 2 == 0): print(n)
    else: print(n - 1)


