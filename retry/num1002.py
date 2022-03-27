testCaseNum = int(input())

for i in range(0, testCaseNum):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r3=((x1-x2)**2+(y1-y2)**2)**(1/2)
    if r1==r2:
        if x1==x2 and y1==y2:
            result = -1
        else:
            if r3<r1+r2:
                result = 2
            elif r3==r1+r2:
                result = 1
            else:
                result = 0
    else:
        if x1==x2 and y1 == y2:
            result=0
        else:
            if r3<r1+r2:
                result=2
            elif r3<max(r1, r2):
                result = 2
            elif r3==r1+r2:
                result = 1
            elif r3==max(r1, r2)-min(r1, r2):
                result = 1
            else:
                result = 0
    print(result)