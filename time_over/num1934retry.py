testCaseNum = int(input())
resultList = []
for i in range(0, testCaseNum):
    a, b = map(int, input().split())
    multiNum = a*b
    factorList = []
    for factor in range(1, min(a, b)+1):
        if min(a, b)%factor==0:
            factorList.append(factor)
    commonFactorList=[]
    for factor in factorList:
        if max(a, b)%factor==0:
            commonFactorList.append(factor)
    result = int(multiNum/max(commonFactorList))
    resultList.append(result)
for result in resultList:
    print(result)