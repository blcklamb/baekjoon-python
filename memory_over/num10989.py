import sys
numList = []
numNum = int(sys.stdin.readline())
for i in range(numNum):
    numList.append(int(sys.stdin.readline()))
numList.sort()
s = ''
for i in numList:
    s += str(i) + '\n'
print(s.strip())