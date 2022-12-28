for i in range(int(input())):
    s, a, b, c = map(int, input().split())

    price = s + (s*c)/100
    if(price >= a and price <= b): print("Yes")
    else: print("No")