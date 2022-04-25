#메모리 초과
import sys
import heapq
num = int(sys.stdin.readline())
numList = []
heapq.heapify(numList)
for _ in range(num):
    heapq.heappush(numList, int(sys.stdin.readline()))

while numList:
    print(heapq.heappop(numList))