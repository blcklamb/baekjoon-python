N = int(input())
houseMap = [[] for _ in range(N)]

for i in range(N):
    rowList = list(map(int, input()))
    houseMap[i] = rowList

def DFS(x, y, hMap, visited):
    global dSize

    visited[x][y] = 1

    dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]

    for d in dir:
        nx = x + d[0]
        ny = y + d[1]

        if nx < 0 or ny < 0 or nx > N-1 or ny > N-1: continue
        if hMap[nx][ny] == 0: continue

        if not visited[nx][ny]:
            dSize += 1
            DFS(nx, ny, hMap, visited)

def tagDanNum(hMap):
    global dSize

    numDanji = 0
    
    visited = []
    for i in range(N):
        visited.append([0 for j in range(N)])

    danjiSize = []
    for i in range(N):
        for j in range(N):
            if hMap[i][j] == 1 and visited[i][j] == 0:
                numDanji += 1

                dSize = 1
                DFS(i, j, hMap, visited)

                danjiSize.append(dSize)
    danjiSize.sort()

    return numDanji, danjiSize

result = tagDanNum(houseMap)
print(result[0])
for i in result[1]:
    print(i)