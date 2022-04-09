import sys
numNum = int(sys.stdin.readline())
inThisList = list(map(int, sys.stdin.readline().split()))
inThisList.sort()
numNum2 = int(sys.stdin.readline())
findThisList = list(map(int, sys.stdin.readline().split()))
findThisList.sort()
for i in findThisList:
    isExist = 0
    for j in inThisList:
        if i==j:
            print(1)
            isExist += 1
            break
    if isExist == 0:
        print(0)
