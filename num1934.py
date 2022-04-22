import sys
def divisor(x):
    divisorList = []
    for i in range(2, x):
        if x%i==0:
            divisorList.append(i)
    return divisorList

def LCM(n, m):
    if max(n, m)%min(n, m)==0:
        return max(n, m)
    elif max(n, m)-min(n, m)==1 and min(n, m) != 1:
        return n*m
    elif (divisor(n)==[] or divisor(m)==[]):
        return n*m
    else:
        commonDivisor=0
        for i in sorted(divisor(min(n,m)), reverse=True):
            if max(n,m)%i==0:
                commonDivisor = i
                break
        if commonDivisor==0:
            return n*m
        else:
            return int(min(n,m)*max(n,m)/commonDivisor)
        
testCaseNum = int(sys.stdin.readline())
for _ in range(testCaseNum):
    n, m = map(int, sys.stdin.readline().split())
    print(LCM(n,m))