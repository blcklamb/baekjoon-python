# 04/07 수업 중 푼 코드 위에 건 시간 초과남
# import sys

# totalCardBag = int(sys.stdin.readline())
# totalCardList = []
# for _ in range(totalCardBag):
#     totalCardList.append(int(sys.stdin.readline()))

# while len(totalCardList)>=2:
#     totalCardList = sorted(totalCardList)
#     minCard = totalCardList.pop(0)
#     minCard2 = totalCardList.pop(0)
#     totalCardList.append(minCard+minCard2)
# print(totalCardList[0])

# heapq와 sorted의 차이 알아보기
import heapq # min heap
import sys

n = int(sys.stdin.readline())
totalCardList = []
for _ in range(n):
    totalCardList.append(int(sys.stdin.readline()))

heapq.heapify(totalCardList)
answer = 0
while len(totalCardList)>=2:
    temp_1 = heapq.heappop(totalCardList)
    temp_2 = heapq.heappop(totalCardList)

    answer += temp_1+temp_2
    heapq.heappush(totalCardList, temp_1+temp_2)

print(answer)
