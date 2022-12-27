def matchingStrings(stringList, queries):
    score = [0] * len(queries)
    for i in range(len(queries)):
        
        for j in range(len(stringList)):
            if stringList[j] == queries[i]: score[i] += 1
    
    print(score)

a = ["aba",
"baba",
"aba",
"xzxb"]
b = [
"aba",
"xzxb",
"ab"
]

matchingStrings(a, b)
