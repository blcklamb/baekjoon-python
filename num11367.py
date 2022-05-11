def letterGrade(score):
    if 0<=score and score<60:
        return 'F'
    elif 60<=score and score<67:
        return 'D'
    elif 67<=score and score<70:
        return 'D+'
    elif 70<=score and score<77:
        return 'C'
    elif 77<=score and score<80:
        return 'C+'
    elif 80<=score and score<87:
        return 'B'
    elif 87<=score and score<90:
        return 'B+'
    elif 90<=score and score<97:
        return 'A'
    else:
        return 'A+'
testCaseNum = int(input())
for _ in range(testCaseNum):
    name, score = input().split()
    print(name, letterGrade(int(score)))