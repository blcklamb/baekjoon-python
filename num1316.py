#전에 손도 못 댔다가 다시 보니 풀려서 남긴 코드
strNum = int(input())

def howManyGroup(str):
    count = 0
    for i in range(len(str)-1):
        if str[i] != str[i+1]:
            count += 1
    return count + 1

def isGroup(str):
    beforeSorted = howManyGroup(str)
    sortedStr = sorted(str)
    afterSorted = howManyGroup(sortedStr)
    if beforeSorted == afterSorted: return True
    else: return False

howManyGroupStr = 0
for i in range(strNum):
    if isGroup(input()):
        howManyGroupStr+=1

print(howManyGroupStr)