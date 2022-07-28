# https://www.acmicpc.net/problem/11279

# 37788 KB 160 ms
from sys import stdin
import heapq
input = stdin.readline

operation = int(input())
heap = []

for _ in range(operation):
    # 음수로 전환하여 큰 수부터 sort하도록 만들기
    this_num = (-1)*int(input())
    if this_num==0:
        print((-1)*heapq.heappop(heap) if len(heap)!=0 else 0)
    else:
        heapq.heappush(heap, this_num)