import sys
sys.setrecursionlimit(100000)

def DFS(x, y, iMap, visited):
    visited[x][y] = 1

    dir = [(1, 0), (0, 1), (-1, 0), (0, -1), (-1, -1), (1, 1), (-1, 1), (1, -1)]
    
    mapH = len(iMap)
    mapW = len(iMap[0])

    for d in dir:
        
        nx = x + d[0]
        ny = y + d[1]

        if nx < 0 or ny < 0 or nx > mapH-1 or ny > mapW-1: continue
        if iMap[nx][ny] == 0: continue

        if not visited[nx][ny]:
            DFS(nx, ny, iMap, visited)

while True:

    mapW, mapH = map(int, input().split())
    if (mapW, mapH) == (0, 0): break
    iMap = []
    visited = []
    num_island = 0

    for i in range(mapH):
        iMap.append(list(map(int, input().split())))
        visited.append([0 for _ in range(mapW)])

    for i in range(mapH):
        for j in range(mapW):
            if iMap[i][j] == 1 and visited[i][j] == 0:
                num_island += 1
                DFS(i, j, iMap, visited)
    print(num_island)