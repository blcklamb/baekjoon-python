# 블로그 참조 hongcoding.tistory.com/72
# 자꾸 딕셔너리로 시작하려는 게 문제


from collections import deque

# 검사하는 배추 좌표의 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

testCase = int(input())

def bfs(graph, a, b):
  queue = deque()
  queue.append((a, b))
  # 검사한 경우 0으로 만들기
  graph[a][b] = 0

  while queue:
    x, y = queue.popleft()
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      if nx < 0 or nx >= bN or ny < 0 or ny >= bM:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
  return

for i in range(testCase):
  count = 0
  bN, bM, bK = map(int, input().split())
  graph = [[0]*bM for _ in range(bN)]

  for j in range(bK):
    x, y = map(int, input().split())
    # 배추가 있는 곳은 1
    graph[x][y] = 1

  for a in range(bN):
    for b in range(bM):
      if graph[a][b] == 1:
        bfs(graph, a, b)
        count += 1
  print(count)


# 덱 안 쓴 거
# 블로그 참조 hongcoding.tistory.com/72
# 자꾸 딕셔너리로 시작하려는 게 문제

# 검사하는 배추 좌표의 상하좌우
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

testCase = int(input())

def bfs(graph, a, b):
  queue = []
  queue.append((a, b))
  # 검사한 경우 0으로 만들기
  graph[a][b] = 0

  while queue:
    x, y = queue.pop(0)
    for i in range(4):
      nx = x+dx[i]
      ny = y+dy[i]
      # 상하좌우가 배추밭 범위 내에 있는 좌표인지 검사
      if nx < 0 or nx >= bN or ny < 0 or ny >= bM:
        continue
      if graph[nx][ny] == 1:
        graph[nx][ny] = 0
        queue.append((nx, ny))
  return

for i in range(testCase):
  count = 0
  bN, bM, bK = map(int, input().split())
  graph = [[0]*bM for _ in range(bN)]

  for j in range(bK):
    x, y = map(int, input().split())
    # 배추가 있는 곳은 1
    graph[x][y] = 1

  for a in range(bN):
    for b in range(bM):
      if graph[a][b] == 1:
        bfs(graph, a, b)
        count += 1
  print(count)