import sys
N, M = map(int, sys.stdin.readline().split())
pokeDic_n = {}
pokeDic_s = {}
for i in range(1, N+1):
    poke = sys.stdin.readline().strip()
    pokeDic_n[i] = poke
    pokeDic_s[poke] = i
print(pokeDic_n)
print(pokeDic_s)
for i in range(M):
    q = sys.stdin.readline().strip()
    if q.isdigit():
        print(pokeDic_n[int(q)])
    if q.isalpha():
        print(pokeDic_s[q])


# https://jennnn.tistory.com/34
