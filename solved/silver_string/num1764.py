import sys

a, b = map(int, sys.stdin.readline().split())

nonSeen = []
nonHeard = []

for _ in range(a):
    nonSeen.append(sys.stdin.readline().rstrip())

for _ in range(b):
    nonHeard.append(sys.stdin.readline().rstrip())

nonSeenHeard = set(nonSeen) & set(nonHeard)

print(len(nonSeenHeard))
for i in sorted(list(nonSeenHeard)):
    print(i)
