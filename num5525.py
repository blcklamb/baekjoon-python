# 리팩토링 조금 하고 제출하면 됨

import sys
pNum = int(sys.stdin.readline())
sLength = int(sys.stdin.readline())
S = sys.stdin.readline()

ioiList = []
tempioi = ''

for i in S:
    if tempioi=='' and i == 'I':
        tempioi += i
    elif tempioi=='' and i == 'O':
        pass
    elif tempioi[-1] != i:
        tempioi += i
    else:
        ioiList.append(tempioi)
        tempioi = i
print('ioiList', ioiList)

def makePN(n):
    PN = 'IOI'
    if n==1:
        return PN
    PN += 'OI'*(n-1)
    return PN
    
pn = makePN(pNum)

def howMany(iois, pNum):
    testN = iois.count('O')
    result = testN + 1 - pNum
    return result

howManyResult = 0
for iois in ioiList:
    howManyResult += howMany(iois, pNum)

print(howManyResult)
