#시간초과

'''
num01, num02 = map(int, input().split())
def isPrimeNum(n):
    index = int(n**(1/2))
    while index>1:
        if n%index==0:
            return False
        index -= 1
    return True
for i in range(num01, num02+1):
    if isPrimeNum(i):
        print(i)
'''
#시간초과
'''
import sys
num01, num02 = map(int, sys.stdin.readline().split())
global primeNumList
primeNumList = {2, 3, 5, 7, 11}
def isPrimeNum(n):
    if n in primeNumList:
        return True
    for i in primeNumList:
        if n%i == 0:
            return False
    index = [i for i in range(2, int(n**(1/2))+1)]
    for i in index:
        if n%i==0:
            return False
        else:
            index = list(filter(lambda x: x%i != 0, index))

    primeNumList.add(n)
    return True

for i in range(num01, num02+1):
    if isPrimeNum(i):
        print(i)

print(primeNumList)
'''

import sys
def isPrimeNum(n):
    factor = 2
    if n == 1:
        return False
    while factor*factor<=n:
        if n%factor == 0:
            return False
        factor +=1
    return True

num01, num02 = map(int, sys.stdin.readline().split())
for i in range(num01, num02+1):
    if isPrimeNum(i)==True:
        print(i)

# 우수 코드
m, n = map(int, input().split())
li = [False] + [True] * ((n - 1) // 2)
for x in range(1, int(n**.5/2+1)):
  if li[x]:
    li[2*x*(x+1)::x*2+1] = [False] * ((((n + 1) // 2) - x * x * 2) // (x * 2 + 1))
if m <= 2:
  print(2)
print('\n'.join([f'{x}' for x, val in zip(range(m+(m&1==0), n+1, 2), li[m//2:]) if val]))
