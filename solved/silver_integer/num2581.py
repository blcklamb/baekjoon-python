M = int(input())
N = int(input())

def isPrimeNum(n):
    if n == 1:
        return False
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n**(1/2))+1):
        if n%i==0:
            return False
    return True

def findPrimeNum(M, N):
    primeList = []
    for i in range(M, N+1):
        if isPrimeNum(i):
            primeList.append(i)
    if primeList == []:
        print(-1)
        return
    print(sum(primeList))
    print(min(primeList))

findPrimeNum(M, N)