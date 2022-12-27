def rotateLeft(d, arr):
    arrB = arr
    temp = []
    for k in range(d):
        temp.append(arr[0])
        for i in range(0, len(arr) - 1):
            arrB[i] = arrB[i + 1]

    for k in range(d):
        arrB[len(arr) - 1 - k] = temp[len(temp) - 1 - k]
        # print(k)
    print(arrB)

def rotateLeft_2(d, arr):
    j = d
    arrB = arr
    temp = []
    for i in range(d):
        temp.append(arrB[i])

    for i in range(len(arr) - d):
        arrB[i] = arrB[j + i]

    for i in range(d):
        arrB[len(arrB) - d + i] = temp[i]
    
    return arrB

rotateLeft_2(2, [1, 2, 3, 4, 5])