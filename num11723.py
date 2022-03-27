import sys
calNum = int(input())
setS = set()

for i in range(calNum):
    #입력받은 데이터 반으로 나누기
    calContent = sys.stdin.readline().split()
    if calContent[0]=='add':
        setNum = int(calContent[1])
        setS.add(setNum)
    elif calContent[0]=='remove':
        #remove할 것이 없을 경우 접근하는 key가 없어 keyError 발생, except로 에러 넘겨버리기
        try:
            setNum = int(calContent[1])
            setS.remove(setNum)
        except KeyError:
            pass
        #int(calContent[1]) in setS ==True False

    elif calContent[0]=='check':
        setNum = int(calContent[1])
        #삼항연산자
        print(1) if setNum in setS else print(0)
    elif calContent[0]=='toggle':
        setNum = int(calContent[1])
        #삼항연산자
        setS.remove(setNum) if setNum in setS else setS.add(setNum)
    elif calContent[0]=='all':
        setS = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
    else:
        setS = set()