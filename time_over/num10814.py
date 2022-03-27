import sys
memberNum = int(sys.stdin.readline())
memberAgeList = []
memberNameList = []



for i in range(memberNum):
    member = sys.stdin.readline().split()
    if len(memberAgeList) == 0: 
        memberAgeList.append(member[0])
        memberNameList.append(member[1])
    else:
        for j in range(len(memberAgeList)):
            if member[0]<memberAgeList[j]:
                memberAgeList.insert(j, member[0])
                memberNameList.insert(j, member[1])
                break
            else:
                memberAgeList.append(member[0])
                memberNameList.append(member[1])

for i in range(len(memberAgeList)):
    print(memberAgeList[i], memberNameList[i])