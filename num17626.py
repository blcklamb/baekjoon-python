# 틀렸습니다!
import sys, math

targetN = int(sys.stdin.readline())

numList = [4]*(targetN+1)

def isSquare(num):
    if num**(1/2) == int(num**(1/2)):
        return True
    return False

def minNum(num):
    if isSquare(num):
        return 1
    for i in range(1, len(numList)):
        if isSquare(i):
            numList[i] = 1
            index = int(i**(1/2))
            while i+index**2<len(numList):
                numList[i+index**2] = 2
                index += 1
            continue
        for j in range(1, math.floor(i**(1/2))+1):
            if numList[i-j**2]+1<numList[i]:
                numList[i] = numList[i-j**2]+1
        # if numList[i]>numList[i-1]+1:
        #     numList[i] = numList[i-1]+1
        
    # for idx, val in enumerate(numList):
    #     print(idx, val)
    return numList[targetN]
print(minNum(targetN))

