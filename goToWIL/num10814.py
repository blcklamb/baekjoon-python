
import sys
N = int(sys.stdin.readline())
memList = []
for _ in range(N):
    age, name = sys.stdin.readline().split()
    memList.append((int(age), name))
sortedMemList = sorted(memList, key=lambda x: x[0])

for age, name in sortedMemList:
    print(age, name)


# 시간 초과 코드
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