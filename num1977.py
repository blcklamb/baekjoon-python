# 완전제곱수 진행 중
# 제출만 하면 됨!

M = int(input())
N = int(input())

def makeSqList(M, N):
    sqList = []
    if int(M**(1/2))**2 == M:
        sqList.append(M)
    if int(M**(1/2)) == int(N**(1/2)):
        return sqList
    for i in range(int(M**(1/2))+1, int(N**(1/2))+1):
        sqList.append(i**2)
    return sqList

result = makeSqList(M, N)
if result:
    print(sum(result))
    print(min(result))
else:
    print(-1)