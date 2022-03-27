numNum = int(input())
numList = list(map(int, input().split()))
realNumList = []
for nums in numList:
    if nums not in realNumList:
        realNumList.append(nums)
    
realNumList.sort()

print(*realNumList)

#우수 코드
input();print(*sorted({*input().split()},key=int))

#우수 코드
import sys

Num=int(sys.stdin.readline().strip())

Numbers=sys.stdin.readline().split()

Numbers=list(set(Numbers))

Numbers=list(map(int,Numbers))

Numbers.sort()

for Number in Numbers:
    print(Number,end=" ")