import sys
matchNum = int(sys.stdin.readline())
count = 0
for i in range(1, matchNum//3+1):
    j = i
    k = matchNum-i-j
    while j<=k:
        if i+j>k:
            count += 1
            j+=1
            k = matchNum-i-j
        else:
            j+=1
            k = matchNum-i-j
print(count)