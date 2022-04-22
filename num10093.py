A, B = map(int, input().split())
if A==B:
    print(0)
    exit()
print(max(A, B)-min(A, B)-1)
for i in range(min(A, B)+1, max(A, B)):
    if i==max(A, B)-1:
        print(i)
        break
    print(i, end=" ")