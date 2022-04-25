import sys
totalLooseMoney=0
while True:
    bettingMoney = int(sys.stdin.readline())
    if bettingMoney == -1:
        print(totalLooseMoney)
        break
    else:
        totalLooseMoney += bettingMoney

#우수 코드
print(sum(map(int,open(0)))+1)