comNum = int(input())
netNum = int(input())

def dfs(graph, startNode):
    count = 0
    # visit = [0]*(comNum+1)과 동일
    visit = []
    stack = []

    stack.append(startNode)

    while stack:
        node = stack.pop()
        if node not in visit:
            visit.append(node)
            stack.extend(graph[node])
            count += 1
    return count

# dfs, bfs에서 그래프 간단히 생성하는 코드
graph = [[]*comNum for _ in range(comNum+1)]
for _ in range(netNum):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

print(dfs(graph, 1)-1)