# case 7까지만 정답, 이후는 시간초과
import sys
def main():
    emp = int(sys.stdin.readline())
    house = list(map(int, sys.stdin.readline().split()))
    officeDic = {}
    minDis = emp*max(house)
    minList = []
    for office in range(min(house), max(house)+1):
        distanceSum = 0
        for employee in house:
            distanceSum += abs(employee-office)
        officeDic[office] = distanceSum
        if minDis>distanceSum:
            minDis = distanceSum
            minList = [office]
        elif minDis==distanceSum:
            minList.append(office)
    print(len(minList))

if __name__=="__main__":
    main()