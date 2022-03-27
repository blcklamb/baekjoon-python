import sys
def listSub(list1, list2):
    for i in list2:
        list1.remove(i)
    return list1
oldList = list(sys.stdin.readline().split())
newList = list(sys.stdin.readline().split())
print(*listSub(newList, oldList))