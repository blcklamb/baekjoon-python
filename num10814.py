from re import L
import sys
N = int(sys.stdin.readline())
memList = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    memList.append((int(age), name))
sortedMemList = sorted(memList, key=lambda x: x[0])

for age, name in sortedMemList:
    print(age, name)