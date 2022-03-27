testCaseNum = int(input())
for i in range(0, testCaseNum):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    r3=((x1-x2)**2+(y1-y2)**2)**(1/2)
    if r1==r2 and r3==0:
        print(-1)
    elif r1+r2==r3 or abs(r1-r2)==r3:
        print(1)
    elif abs(r1-r2) < r3 < (r1+r2):
        print(2)
    else:
        print(0)