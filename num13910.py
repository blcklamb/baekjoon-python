
# 첫 번째 줄: 짜장면의 수 N(1, 10001), 웍의 수 M(1, 101)
# 두 번째 줄: 웍의 크기 S(1, N+1) M개
# 같은 크기의 웍을 여러 개 가지고 있을 수 있음

# 출력: 최소 요리 횟수
# 모든 주문을 처리할 수 없는 경우 -1

'''
5 2
1 3
>>>2
6 2
1 3
>>>2
SList = [s1, s2, s3, ...]
N = (s1+ s2 + s3)+(s2 + s3)+...
T(N) = 최소 횟수
T(N-min())
T(1) 

N%sum(SList)==0 T(N) = N//sum(SList)
그 외의 경우만 따지자,
N//max(SList) 가 곧 T(N)이 됨
1 3인 경우
    1     3
7   1     2  
9   0     3 
10  1     3
11  2     3
13  1     4 
14  2     4
15  0     5 T(N) = T(N-(s1+s2)) + 1 

2 3인 경우
    2   3
1           -1
2   1   0
3   0   1
4   2   0
6   0   2
7   2   1
8   1   2
9   0   3    
10  2   2
11  1   3
12  0   4
    3   2
13      T(N) = T(N-(s1+s2))+1  3  
        T(N) = T(N-s1) + 1     4 
        T(N) = T(N-s2) + 1     3

2 3 4 인 경우
    2   3   4
3       1
4           1
5   1   1   0
6   1       1
7       1   1
8           2
9   1   1   1
10  1       2
11      1   2
12  2       2 T(N) = T(N-(s1+s2+s3)) + 1 2
              T(N) = T(N-(s1+s2)) + 1    2
              T(N) = T(N-(s2+s3)) + 1    2
              T(N) = T(N-(s1+s3)) + 1    2
              T(N) = T(N-s1) + 1         3
              T(N) = T(N-s2) + 1         2
              T(N) = T(N-s3) + 1         3 
13            T(N) = T(N-(s1+s2+s3)) + 1 2
              T(N) = T(N-(s1+s2)) + 1    3
              T(N) = T(N-(s2+s3)) + 1    2
              T(N) = T(N-(s1+s3)) + 1    2
              T(N) = T(N-s1) + 1         3
              T(N) = T(N-s2) + 1         3
              T(N) = T(N-s3) + 1         2 
'''

import sys

N, M = map(int, sys.stdin.readline().split())
sList = list(map(int, sys.stdin.readline().split()))

def cookingCount(N, sList):
    countList = [[0 for _ in range(M)] for _ in range(N+1)]
    
    for i in range(1, sum(sList)+1):
        sCountList = [0 for _ in range(M)]
        if i<min(sList):
            countList[i] = 0

    
cookingCount(N, sList)