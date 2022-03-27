import numpy
from collections import Counter

num = int(input())
numList = []
for i in range(0, num):
    numList.append(int(input()))
arithmetic=round(numpy.mean(numList))
median=round(numpy.median(numList))
count = Counter(numList)
mode = count.most_common(1)[0][0]
round = max(numList)-min(numList)
print(arithmetic, median, mode, round, sep='\n')