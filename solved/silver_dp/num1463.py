'''
X % 3 == 0 -> //3
X % 2 == 0 -> //2
X -> - 1

1로 만들기, 연산을 사용해서 1로 만들기
연산을 사용하는 횟수의 최솟값 출력

T(N) = T(N-1) + 1
T(N) = T(N//2) + 1
'''

'''
메모리 38652KB 시간 556ms
'''
'''
import sys
input = sys.stdin.readline

def makeOp(num):
    opNum = [0]*(num+1)
    if num == 1:
        return 0
    if num == 2 or num == 3:
        return 1
    opNum[2] = 1
    opNum[3] = 1
    
    for i in range(4, num+1):
        tmpNum = i
        tmpNum = tmpNum - 1
        opNum[i] = opNum[tmpNum]+1
        if i%2==0:
            opNum[i] = min(opNum[tmpNum]+1, opNum[i//2]+1)
            tmpNum = i//2
        if i%3==0:
            opNum[i] = min(opNum[tmpNum]+1, opNum[i//3]+1)
            tmpNum = i//3
    return opNum[num]

num = int(input())
print(makeOp(num))
'''
'''
가장 처음 제출한 코드
메모리 39088 KB, 508ms
'''
'''
N = int(input())

def minOpe(num):
    
    T = [0 for _ in range(num+4)]
    T[1] = 0
    T[2] = 1
    T[3] = 1

    for i in range(4, num+4):
        T[i] = T[i-1]+1
        if i%2==0:
            T[i] = min(T[i], T[i//2]+1)
        if i%3==0:
            T[i] = min(T[i], T[i//3]+1)
    
    return T[num]

print(minOpe(N))
'''
'''
둘이 합쳐서 제출한 코드
메모리 38652KB 시간 500ms
'''
import sys
input = sys.stdin.readline

def makeMinOp(num):
    opNum = [0]*(num+4)

    opNum[1] = 0
    opNum[2] = 1
    opNum[3] = 1

    for i in range(4, num+4):
        opNum[i] = opNum[i-1]+1
        if i%2==0:
            opNum[i] = min(opNum[i], opNum[i//2]+1)
        if i%3==0:
            opNum[i] = min(opNum[i], opNum[i//3]+1)
    return opNum[num]

print(makeMinOp(int(input())))