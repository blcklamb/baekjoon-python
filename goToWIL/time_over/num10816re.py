import sys
from collections import Counter
cardNum = int(sys.stdin.readline())
cardList = sorted(list(map(int, sys.stdin.readline().split())))
findNum = int(sys.stdin.readline())
findList = list(map(int, sys.stdin.readline().split()))
cardCounter = Counter(cardList)

def howMany(list, num):
    start = 0
    end = len(list)
    if list[0]>num or list[-1]<num:
        return 0
    while end-start>=0:
        mid = int((start+end)/2)
        if list[mid]==num:
            return cardCounter[num]
        elif list[mid]>num:
            end=mid-1
        else:
            start=mid+1
    return 0

answer = ''
for i in findList:
    answer += ' ' + str(howMany(cardList, i))
print(answer.strip())