import sys
def isPrime(num):
    factor=2
    if num == 1:
        return False
    while factor<num:
        if num%factor==0:
            return False
        factor+=1
    return True

num = int(input())
numList = list(map(int, sys.stdin.readline().split()))    
howManyPrimeNum = 0
for i in numList:
    if isPrime(i)==True:
        howManyPrimeNum += 1
print(howManyPrimeNum)