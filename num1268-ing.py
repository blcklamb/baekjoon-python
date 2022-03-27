import sys
studentNum = int(sys.stdin.readline())

studentList = []
firstGradeClassList = [0]*10
secondGradeClassList = [0]*10
thirdGradeClassList = [0]*10
fourthGradeClassList = [0]*10
fifthGradeClassList = [0]*10
for i in range(studentNum):
    studentClass = "".join(sys.stdin.readline().strip().split())
    for classNum in range(5):
        studentClassNum = int(studentClass[classNum])
        if classNum==0: firstGradeClassList[studentClassNum]+=1
        elif classNum==1: secondGradeClassList[studentClassNum]+=1
        elif classNum==2: thirdGradeClassList[studentClassNum]+=1
        elif classNum==3: fourthGradeClassList[studentClassNum]+=1
        else: fifthGradeClassList[studentClassNum]+=1
    studentList.append(studentClass)


for i in 

print(studentList)
print(firstGradeClassList)
print(secondGradeClassList)
print(thirdGradeClassList)
print(fourthGradeClassList)
print(fifthGradeClassList)
