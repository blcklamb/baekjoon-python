comNum = int(input())
netNum = int(input())

def bfs(graph, startNode):
    count = 0
    visit = [0]*(comNum+1)
    queue = []

    queue.append(startNode)

    while queue:
        node = queue.pop(0)
        if node not in visit:
            visit.append(node)
            queue.extend(graph[node])
            count += 1
    return count

graph = [[]*comNum for _ in range(comNum+1)]
for _ in range(netNum):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(graph)

print(bfs(graph, 1)-1)