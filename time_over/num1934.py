testCaseNum = int(input())
a, b = map(int, input().split())
factorList = []
for factor in range(1, min(a, b)+1):
    if min(a, b)%factor==0:
        factorList.append(factor)
commonFactorList=[]
for factor in factorList:
    if max(a, b)%factor==0:
        commonFactorList.append(factor)
commonFactorList.reverse()
multipleList=[]
if commonFactorList==[1]:
    print(a*b)
else:
    while True:
        for commonFactor in commonFactorList:
            if a%commonFactor!=0 or b%commonFactor!=0:
                multipleList.append(a)
                multipleList.append(b)
                break
            else:
                a=a//commonFactor
                b=b//commonFactor
                print(a, b)
                multipleList.append(commonFactor)
        break
    allMultiple = 1
    print(multipleList)
    for i in multipleList:
        allMultiple *= i
    print(allMultiple)