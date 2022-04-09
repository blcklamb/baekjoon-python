#드디어 맞음
# https://somjang.tistory.com/entry/Mxmxmxm
import sys
num = int(sys.stdin.readline())
numList = [0] * 10001
for _ in range(num):
    getNum = int(sys.stdin.readline())
    numList[getNum] += 1

index = 0

for i in range(10001):
    if numList[i] !=0:
        for _ in range(numList[i]):
            print(i)

        