N = int(input())

def makeTile(N):
    memo = [0 for _ in range(N+2)]
    memo[1] = 1
    memo[2] = 2
    if N<=2:
        return memo[N]
    for i in range(3, N+1):
        memo[i] = memo[i-1]+memo[i-2]
    return memo[N]

print(makeTile(N)%10007)

# recursionError와 시간 초과
def makeTile2(N):
    if N==1:
        return 1
    if N==2:
        return 2
    return makeTile2(N-1)+makeTile2(N-2)

print(makeTile2(N)%10007)
