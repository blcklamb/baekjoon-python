# 미완성

import sys
input = sys.stdin.readline

houseN = int(input())

colorInfo = [[]]

for _ in range(houseN):
    R, G, B = map(int, input().split())
    colorInfo.append([R, G, B])
    
print(colorInfo)

'''

F[N] 최소 비용
h{N} N번째 집 색상 비용 리스트
T[2] = min(min(h1)+min(h2)(if h1.index(min(h1)) != h2.index(min(h2)) ))
T[3] = 

'''
colorName = ['R', 'G', 'B']
def minPaint(num):
    colorFix = [0]*(num+1)
    costList = [0]*(num+1)

    colorFix[1] = colorName[colorInfo[1].index(min(colorInfo[1]))]
    costList[1] = min(colorInfo[1])
    print(colorFix, costList)
    for i in range(2, num+1):
        if colorFix[i-1] == colorName[colorInfo[i].index(min(colorInfo[i]))]:
            # stick = costList[i-1]+
            costList[i] = min(costList[i-1]+min)
minPaint(houseN)