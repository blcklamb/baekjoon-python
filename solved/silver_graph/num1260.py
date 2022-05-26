from sys import stdin
from collections import deque

vertexN, lineN, startV = map(int, stdin.readline().split())

nodeInfo = [[] for _ in range(vertexN+1)]

for _ in range(lineN):
    vertexA, vertexB = map(int, stdin.readline().split())
    nodeInfo[vertexA].append(vertexB)
    nodeInfo[vertexB].append(vertexA)

for nodes in nodeInfo:
    nodes.sort()

def DFS(root):
    visited = []
    stack = [root]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if nodeInfo[node]:
                stack += sorted(nodeInfo[node], reverse=True)
    return visited

def BFS(root):
    visited = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += nodeInfo[node]
    return visited

print(*DFS(startV))
print(*BFS(startV))
     

