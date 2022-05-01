vowelList = ['A','E','I','O','U','a','e','i','o','u']
testCaseNum = int(input())

def countVowel(str):
    str = str.replace(" ", "")
    count = 0
    total = len(str)
    for i in str.replace(" ", ""):
        if i in vowelList:
            count += 1
    return count, total-count

for _ in range(testCaseNum):
    a, b = countVowel(input())
    print(b, a)
