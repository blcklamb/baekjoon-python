M = int(input())
N = int(input())

answer = 0
answer02 = 0
if M != 1 and int(M**(1/2)) == int(N**(1/2)):
    print(-1)
    exit()
elif M ==1 and N ==1:
    answer = 1
    answer02 = 1
else:
    for i in range(int(M**(1/2))+1, int(N**(1/2))+1):
        if M==1:
            answer02=1
            answer += 1
        elif i == int(M**(1/2))+1:
            answer02 = i**2
        answer += i**2

print(answer)
print(answer02)