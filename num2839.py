sugarW = int(input())

#5kg짜리 봉지는 fiveBag, 3kg짜리 봉지는 threeBag
fiveBag = 0
threeBag = 0

while True:
    #5kg짜리로 최대한 포장하고 남은 것이 3kg로 나눠떨어질 때 계산
    if (sugarW%5)%3==0:
        fiveBag = sugarW//5
        threeBag += (sugarW-fiveBag*5)//3
        totalBag = fiveBag+threeBag
        break
    #그렇지 않으면 원래 5kg로 나누면 나오는 몫에서 -1씩 하기
    else:
        #나누다가 결국엔 나머지가 1, 2, 4, 7인 경우는 3, 5kg로 포장이 안되므로 -1 출력
        if sugarW==1 or sugarW==2 or sugarW==4 or sugarW==7:
            totalBag = -1
            break
        else:
            threeBag += 1
            sugarW -= 3

print(totalBag)

#우수코드
N = int(input())
cnt = 0
while True:
    if (N % 5) == 0:
        cnt = cnt + (N // 5)
        print(cnt)
        break
    N -= 3
    cnt += 1
    if N < 0:
        print(-1)
        break