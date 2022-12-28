for i in range(int(input())):
    u, v, a, s = map(int, input().split())
    
    vf = u**2 - 2*a*s

    if vf > v**2 : print("No")
    else: print("Yes")