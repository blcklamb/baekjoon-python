'''
N, M, B (1<=M, N<=500, 0<=B<=6.4*10^7)
i+2번째 줄의 i+1번째 수 = (i, j)
0<=땅의 높이<=256

    1. 좌표 (i, j)의 가장 위에 있는 블록 제거, 인벤토리에 넣기(2초)
    2. 인벤토리에서 블록 하나 꺼내어 좌표 (i, j)의 가장 위에 있는 블록 위에 놓기(1초)

땅 고르는 데 걸리는 시간, 땅의 높이
(답 여러 개 있으면 그중에서 땅의 높이가 가장 높은 것)

경우의 수
1) 채우기만 할 때
    인벤토리 충분해야함
    땅의 높이는 max()
2) 파기만 할 때
3) 채우고 팔 때 
파거나 채울 때 데 순서 없으므로
땅의 높이를 정하고 각각의 시간과 인벤토리를 계산하면 될 듯

땅 높이 리스트 = D
1) 땅의 높이=max(D)-> 채우기만 함
    인벤토리 충분한 지 확인

2) 땅의 높이= min(D)-> 파기만 함

3) min(D)<땅의 높이<max(D)->파는 것 먼저 하고 채우는 것 나중에 계산

'''

import sys

N, M, B = map(int, sys.stdin.readline().split())
mapList = []

maxHeight = 0
minHeight = 256

answer = ()

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    mapList.append(row)
    maxHeight = max(maxHeight, max(row))
    minHeight = min(minHeight, min(row))

print(mapList, maxHeight, minHeight)

howManyFill = 0
for i in range(N):
    for j in range(M):
        if mapList[i][j]<maxHeight:
            howManyFill += maxHeight - mapList[i][j]
if howManyFill<B:
    answer = (howManyFill, maxHeight)

howManyDig = 0
for i in range(N):
    for j in range(M):
        if mapList[i][j]>minHeight:
            howManyDig += mapList[i][j] - minHeight
answer = (howManyDig*2, minHeight)

howManyFill = 0
howManyDig = 0
for k in range(minHeight+1, maxHeight):
    for i in range(N):
        for j in range(M):
            if mapList[i][j]<k:


# 인벤토리 고려... 어렵네........
# 채우고 파아야하는 경우 삼중 for문이라 벌써 걱정된다