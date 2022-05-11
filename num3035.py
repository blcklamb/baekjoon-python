
'''
R, C, ZR, ZC = map(int, input().split())
mapList = [[] for _ in range(C)]
for i in range(R):
    mapList[i] = list(input())
newMapList01 = [[] for _ in range(C)]
for i in range(R):
    for j in range(C):
        newMapList01[i].append(mapList[i][j]*ZC)

newMapList02 = []
for j in newMapList01:
    for _ in range(ZR):
    
        newMapList02.append(j)

for i in newMapList02:
    print(*i, sep='')
'''

i = 0
new = []
res = ''
a, b, c, d = map(int, input().split())
for i in range(a):
    article = input()
    for k in range(c):
        for j in range(b):
            res += article[j] * d
        new.append(res)
        res = ''
for i in new:
    print(i)