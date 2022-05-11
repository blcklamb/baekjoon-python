def main():
    emp = int(input())
    house = list(map(int, input().split()))
    officeDic = {}
    count = 0
    for office in range(max(house)):
        distanceSum = 0
        for employee in house:
            distanceSum += abs(employee-office)
        officeDic[office] = distanceSum
    print(min(officeDic.values()))
    for officeSpot, distance in enumerate(officeDic):
        print(officeSpot, distance)
        if distance == min(officeDic.values()):
            count +=1
    
    print(count)

if __name__=="__main__":
    main()