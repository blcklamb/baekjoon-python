'''
3층일 떄,
세 개의 경우의 수의 합이 나오도록,
예를 들면 3층의 두번째 수를 마지막으로 더할 때
경우의 수는 2개인데, 둘 중 최대인 것으로 저장하도록 만들기
'''

import sys
input = sys.stdin.readline

triN = int(input())
triDic = {}
for i in range(1, triN+1):
    triDic[i] = list(map(int, input().split()))

def makeSum(dic):
    for i in range(1, triN):
        for j in range(i+1):
            if j == 0:
                dic[i+1][j] += dic[i][j]
            elif j == i:
                dic[i+1][j] += dic[i][j-1]
            else:
                dic[i+1][j] += max(dic[i][j-1], dic[i][j])
    return max(dic[triN])

print(makeSum(triDic))

"""
메모리 34044 KB	시간 160ms
핫쉬 시간 너무 잘했잖아?
"""