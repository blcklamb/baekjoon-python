num = int(input())
numList = []
def arithmetic(list):
    mean=sum(list)/len(list)
    return round(mean)
def median(list):
    list.sort()
    return list[len(list)//2]
def mode(list):
    list.sort()
    if len(list)==1:
        return list[0]
    else:
        maxList = abs(max(list))
        minList = abs(min(list))
        modeCountList = [0]*(minList+1+maxList)
        for i in list:
            modeCountList[i+minList] += 1
        if modeCountList.count(max(modeCountList)) != 1:
            modeNum = 0
            mostNum = min(list)-1
            for i in modeCountList:
                mostNum += 1
                if i == max(modeCountList):
                    modeNum += 1
                if modeNum == 2:
                    return mostNum
        else: 
            print(modeCountList.index(max(modeCountList)))
            return modeCountList.index(max(modeCountList))
        
def rangeNum(list):
    return max(list)-min(list)

for i in range(0, num):
    numList.append(int(input()))

print(arithmetic(numList), median(numList), mode(numList), rangeNum(numList), sep='\n')