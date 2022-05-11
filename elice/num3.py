def main():
    N, M = map(int, input().split())
    arrowMap = []
    for _ in range(N):
        rowList = list(map(int, input().split()))
        arrowMap.append(rowList)
    start = list(map(int, input().split()))
    
    dirList = [(-1,0), (0, -1), (0, 1), (1, 0)]
    # 1 상 2 좌 3 우 4 하
    record = [start]
    while True:
        if start[0]>N or start[0]<0 or start[1]>M or start[1]<0:
            print(-1)
            return
        direction=arrowMap[start[0]-1][start[1]-1]

        start = [start[0] + dirList[direction-1][0], start[1]+dirList[direction-1][1]]
        if start in record:
            print(len(record)-record.index(start))
            return
        else:
            record.append(start)

if __name__=="__main__":
    main()