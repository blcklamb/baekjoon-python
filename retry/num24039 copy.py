limitNum = int(input())
def primeNumber(limit):
    primeNumberList = []
    for num in range(2, limit+1):
        for i in primeNumberList:
            if num%i == 0 and i*i<=num:
                break
        else:
            primeNumberList.append(num)
    return primeNumberList

for i in range(0, limitNum+1):
    if i*i>=limitNum:
        limitNum2=i+10
        break

primeNumberList=primeNumber(limitNum2)
primeNumberMultiList = []

for i in range(0, len(primeNumberList)-1):
    multiNum=primeNumberList[i]*primeNumberList[i+1]
    primeNumberMultiList.append(multiNum)
for num in primeNumberMultiList:
    if num>limitNum:
        print(num)
        break