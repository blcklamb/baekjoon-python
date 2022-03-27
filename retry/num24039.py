def isPrimeNum(num):
    orNot = 0
    if num == 1:
        return True
    else:
        for i in range(1, num+1):
            if num%i==0:
                orNot += 1
    if orNot >2:
        return False
    else:
        return True
primeNumList=[]
primeNumMultiList=[]
for i in range(1, 150):
    if isPrimeNum(i)==True:
        primeNumList.append(i)
for j in range(0, len(primeNumList)-1):
    primeNumMultiList.append(primeNumList[j]*primeNumList[j+1])
num = int(input())
if num == 1:
    print(2)
for k in range(0, len(primeNumMultiList)-1):
    if primeNumMultiList[k]<=num<primeNumMultiList[k+1]:
        print(primeNumMultiList[k+1])