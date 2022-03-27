import sys

def stackPut(n, sequence):
    stack = []
    num = 1
    index = 0
    result = []

    while True:
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1
        elif sequence[index] == stack[-1]:
            stack.pop()
            result.append("-")
            index += 1
            if index == n:
                break
        else:
            stack.append(num)
            result.append("+")
            num += 1
    if len(stack) == 0:
        print(*result, sep="\n")

totalNum = int(sys.stdin.readline())
numList = []
for i in range(totalNum):
    numList.append(int(sys.stdin.readline()))

# 최댓값 이후로 내림차순 아니면 NO
checkList = numList[numList.index(max(numList)):]
if checkList != sorted(checkList, reverse=True):
    print("NO")

stackPut(totalNum, numList)
