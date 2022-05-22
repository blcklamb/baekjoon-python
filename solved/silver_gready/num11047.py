N, K = map(int, input().split())
coinList = []
for _ in range(N):
    coinList.append(int(input()))

useCoinList = [x for x in coinList if x<=K]

index = len(useCoinList)-1
coinCount = 0
while True:
    if K == 0 or index < 0:
        break
    if useCoinList[index] <= K:
        
        coinCount += K//useCoinList[index]
        K -= useCoinList[index]*(K//useCoinList[index])
        index -= 1
    else:
        index -= 1

print(coinCount)