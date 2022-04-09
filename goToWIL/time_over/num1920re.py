import sys
num01 = int(sys.stdin.readline())
numList01 = sorted(list(map(int, sys.stdin.readline().split())))
num02 = int(sys.stdin.readline())
numList02 = list(map(int, sys.stdin.readline().split()))

def binarySearch(list, num):
    start = 0
    end = len(list)
    while end-start>=0 :
        mid = int((start+end)/2)
        # 핫쉬 여기서틀림
        # if mid>=len(list):
        #     break
        if list[-1]<num:
            break
        if list[mid] == num:
            return 1
        elif list[mid]>num:
            end = mid -1
        else:
            start = mid +1
    return 0

for i in numList02:
    print(binarySearch(numList01, i))