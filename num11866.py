# 네 번이나 틀렸습니다 뜸...
# 뭐가 문제인지 모르겠음
N, K = map(int, input().split())

numList = [i for i in range(1, N+1)]

def josephus(getList, key):
    out = []
    # key를 인덱스로 활용하기 위해 -1
    key -= 1
    # getList에서 하나씩 빼서 out으로 넣기
    while getList != None:
        # 마지막 하나 남은 경우 그대로 빼기
        if len(getList) == 1:
            out.append(getList.pop())
            break
        # key 값이 전체 길이보다 긴 경우 임시 key값 만들기
        tempKey = 0
        if key > len(getList):
            tempKey = tempKey % len(getList)
            if tempKey == 0:
                tempKey = tempKey + len(getList)
            tempKey -= 1
            out.append(getList.pop(tempKey))
        # key 값이 전체 길이보다 작은 경우 돌려서 
        else:
            getList = getList[key:]+getList[:key]
            out.append(getList.pop(0))
    return out

print(str(josephus(numList, K)).replace('[', '<').replace(']', '>'))