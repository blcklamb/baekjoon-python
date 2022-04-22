# https://www.acmicpc.net/problem/2164
# 시간초과
'''
num = int(input())
queue = [i for i in range(1, num+1)]

while len(queue)>1:
    queue.pop(0)
    
    queue = queue[1:]+[queue[0]]
print(*queue)
'''
from collections import deque

card = deque()
num = int(input())
queue = [i for i in range(1, num+1)]
card.extend(queue)

for _ in range(num-1):
    card.popleft()
    temp = card.popleft()
    card.append(temp)

print(*card)

# 우수 코드
n = int(input())
s = 1
while True:
    if s * 2 > n:
        break
    else:
        s *= 2
if n == s:
    print(s)
else:
    print(n - (s - (n - s)))