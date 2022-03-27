import sys

nodeNum, ksPoint, power = map(int, sys.stdin.readline().split())
nodeInfo = 1

# 인접한 노드로 딕셔너리 만들기
adjac={}

for i in range(1, nodeNum+1):
    adjac[i] = []

while nodeInfo<nodeNum:
    # 1 2
    node01, node02 = map(int, sys.stdin.readline().split())
    adjac[node01].append(node02)
    adjac[node02].append(node01)
    nodeInfo+=1

print(adjac)

visited = []
queue = [1]

adjac={
    1: [2], 
    2: [1, 3, 4], 
    3: [2, 5], 
    4: [2], 
    5: [3, 6], 
    6: [5]
}
global completeNode
completeNode = []
def throwComplete(currentNode, power):
    global completeNode
    queue=[currentNode]
    while power>0:
        while queue:
            checkNode = queue.pop(0)
            completeNode.append(checkNode)
            for adjacNode in adjac[checkNode]:
                queue.append(adjacNode)
            power-=1
    return completeNode
print(throwComplete(2, 1))
completeNode=[]
print(throwComplete(3, 1))
completeNode=[]
print(throwComplete(2, 2))
completeNode=[]
print(throwComplete(3, 2))

#인접한 노드 딕셔너리로 총 경로 만들기
def bfsQueue(adjac, startNode):
    queue = [startNode]
    visited = []

    while queue:
        currentNode = queue.pop(0)
        visited.append(currentNode)
        for adjacNode in adjac[currentNode]:
            if adjacNode not in visited:
                queue.append(adjacNode)
    return visited
