T = int(input())

while(T > 0):
    A, B, X = map(int, (input().split()))

    years = (B - A)/X
    print(years)
    T -= 1
