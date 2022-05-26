from sys import stdin
vertexN, lineM = map(int, stdin.readline().split())

nodeInfo = [[] for _ in range(vertexN+1)]

for _ in range(lineM):
    vertexA, vertexB = map(int, stdin.readline().split())
    nodeInfo[vertexA].append(vertexB)
    nodeInfo[vertexB].append(vertexA)

#43833832
'''
def DFS(start):
    d_visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in d_visited:
            d_visited.append(node)
            if nodeInfo[node]:
                stack += nodeInfo[node]
    return d_visited 

connect_component = 0

visited = []
for i in range(1, vertexN+1):
    if i not in visited:
        connect_component += 1
        visited += DFS(i)

print(connect_component)
'''
#43833953
'''
def BFS(start):
    queue = [start]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += nodeInfo[node]

connect_component = 0

visited = []
for i in range(1, vertexN+1):
    if i not in visited:
        connect_component += 1
        BFS(i)

print(connect_component)
''' 
#43833832
'''
def DFS(start):
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if nodeInfo[node]:
                stack += nodeInfo[node]

connect_component = 0

visited = []
for i in range(1, vertexN+1):
    if i not in visited:
        connect_component += 1
        DFS(i)

print(connect_component)
'''
# 시간을 줄일 수 있는 방법 또 없을까...