# 제출만 하면 됨
# 제출 완료

testCase = int(input())

def wave(n):
    waveList = [0, 1, 1, 1, 2, 2]
    if n>5:
        for _ in range(n-5):
            newValue = waveList[-1]+waveList[-5]
            waveList.append(newValue)
    return waveList[n]
            

for _ in range(testCase):
    print(wave(int(input())))