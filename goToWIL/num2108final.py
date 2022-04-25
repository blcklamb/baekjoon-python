# numpy 사용 불가

import sys
from collections import Counter

num = int(sys.stdin.readline())
numList = []
for _ in range(num):
    numList.append(int(sys.stdin.readline()))

arithmetic = round(sum(numList)/num)
median = sorted(numList)[num//2]

count = Counter(numList)

countSorted = sorted(count.most_common(), key=lambda x:(-x[1], x[0]))

if num==1:
    mode = numList[0]
elif countSorted[0][1]!=countSorted[1][1]:
    mode = countSorted[0][0]
else:
    mode = countSorted[1][0]
round = max(numList)-min(numList)
print(arithmetic)
print(median)
print(mode)
print(round)
