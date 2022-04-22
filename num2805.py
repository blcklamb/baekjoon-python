import sys


def findMaxHeight(M, H, height):

    start = 0
    end = height 
    while start <= end:
        mid = (start+end)//2
        sawedWood = 0
        for i in H:
            if i-mid>0:
                sawedWood += (i-mid)
        if sawedWood == M:
            return mid
        elif sawedWood  > M:
            start = mid + 1
        else:
            end = mid - 1
    if sawedWood>M:
        return mid
    else:
        return mid-1
            

N, M = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))
height = max(H)
print(findMaxHeight(M, H, height))