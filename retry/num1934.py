import sys

def primeNumber(num):
    if num != 1:
        for f in range(2, num):
            if num % f == 0:
                return False
    else:
        return False
    return True

def divNum(num1, num2):
    for j in range(1, min(num1, num2)+1):
        if primeNumber(j)==True:
            if num1%j==0 and num2%j==0:
                count = 0
                while num1%j==0 and num2%j==0:
                    num1=num1/j
                    num2=num2/j
                    count += 1
                factorList.append(pow(j, count))
    
testCaseNum = int(sys.stdin.readline())
resultList = []
for i in range(testCaseNum):
    num1, num2 = map(int, sys.stdin.readline().split())
    factorList = []
    divNum(num1, num2)
    basicFactor = 1
    for k in factorList:
        basicFactor *= k
    factor1 = num1/basicFactor
    factor2 = num2/basicFactor
    result = basicFactor*factor1*factor2
    resultList.append(result)
s = ''
for results in resultList:
    s += (str(int(results))+ '\n')
print(s)