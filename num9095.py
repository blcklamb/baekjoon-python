'''
T(N) = T(N-1)+T(N-2)+T(N-3)
T(1) = 1
T(2) = 2
T(3) = 4
T(4) = 1 1 1 1/2 1 1/1 2 1/3 1
       1 1 2/2 2
       1 3

'''
def makeCase(N):
    T = [[0] for _ in range(N+3)]
    T[1] = 1
    T[2] = 2
    T[3] = 4
    if N<=3:
        return T[N]
    for i in range(4, N+1):
        T[i] = T[i-1]+T[i-2]+T[i-3]
    return T[N]

testCaseNum = int(input())
for _ in range(testCaseNum):
    print(makeCase(int(input())))