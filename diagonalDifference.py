def diagonalDifference(arr):
    a = 0
    b = 0
    for i in range(0, len(arr)):
        a += arr[i][i]
        j = len(arr) - i - 1
        b += arr[i][j]
        print(b)
    return abs(b - a)
[1, 3]
[2, 2]
[3, 1]
diagonalDifference([[1,2,3], [4,5,6],[9,8,9]])