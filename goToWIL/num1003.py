# 시간초과난 코드
# testCaseNum = int(input())

# def fibo(n, z, o):
#     if n==0:
#         return (0, z+1, o)
#     if n==1:
#         return (1, z, o+1)
#     num1, z1, o1 = fibo(n-1, z, o)
#     num2, z2, o2 = fibo(n-2, z, o)
#     return (num1+num2, z1+z2, o1+o2)
        

# for _ in range(testCaseNum):
#     num, z, o =  fibo(int(input()),0, 0)
#     print(z, o)

# 참고 https://jennnn.tistory.com/11
# 성공한 코드
testCaseNum = int(input())

for _ in range(testCaseNum):
    n = int(input())
    count0 = [1, 0]
    count1 = [0, 1]

    for i in range(2, n+1):
        count0.append(count0[i-1]+count0[i-2])
        count1.append(count1[i-1]+count1[i-2])
    print(count0[n], count1[n])