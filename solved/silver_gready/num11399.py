# 제출만 하면 됨

pplNum = int(input())
timeList = list(map(int, input().split()))

sortedTimeList = sorted(timeList)

totalTime = 0
for i, t in enumerate(sortedTimeList):
    totalTime += t*(pplNum-i)

print(totalTime)