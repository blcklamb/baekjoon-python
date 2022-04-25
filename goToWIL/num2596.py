#짱구 돌리느라 힘들어서 남긴 코드

strNum = int(input())
secretLetter = input()
decodeList = ['000000','001111','010011','011100','100110','101001','110101','111010']
decodeLetterList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
letterList = []
def findRealLetter(sixNum):
    wrongCountList = []
    
    for decode in decodeList:
        wrongCount = 0
        for i in range(0, 6):
            if sixNum[i]!=decode[i]:
                wrongCount += 1
        wrongCountList.append(wrongCount)
    if 1 in wrongCountList:
        result = decodeLetterList[wrongCountList.index(min(wrongCountList))]
    else:
        result = False
    return result


a=0
b=6
for i in range(0, strNum):
    letterList.append(secretLetter[a:b])
    a += 6
    b += 6
decodeStr = ''
letterBreak = True
for letter in letterList:
    for realLetter in decodeList:
        if letter in decodeList:
            if letter==realLetter:
                decodeStr += decodeLetterList[decodeList.index(realLetter)]
                break
        else:            
            if findRealLetter(letter) == False:
                decodeStr=letterList.index(letter)+1
                letterBreak = False
                break
            else:
                decodeStr += findRealLetter(letter)
                break
    if letterBreak == False:
        break
print(decodeStr)

