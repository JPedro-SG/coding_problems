def arrayManipulation(n, queries):
    list = [0] * (n + 1)
    for querie in queries:
        [a,b,k] = querie
        list[a - 1] += k
        list[b] -= k
        # print(list)
    
    maxSum = 0
    sum = 0
    for item in list:
        sum += item
        if(sum > maxSum): maxSum = sum
    return maxSum
    
    

x = arrayManipulation(10, 
    [[1, 5, 3],
    [4, 8, 7],
    [6, 9, 1]])

print(x)