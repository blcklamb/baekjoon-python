# sorted 사용법 메모하기
import sys

N = int(sys.stdin.readline())

spotList = []
for _ in range(N):
    x, y = map(int, sys.stdin.readline().split())
    spotList.append((x, y))

def multisort(item):
    return (item[1], item[0])

sortedList = sorted(spotList, key=multisort)
for x, y in sortedList:
    print(x, y)