import sys
numNum = int(sys.stdin.readline())
numStr = ''
for i in range(0, numNum):
    numStr += sys.stdin.readline()
numList=list(map(int, numStr.strip().split('\n')))
numList.sort()
for i in numList:
    print(i)