colorPaperNum = int(input())

totalColorPaper = set()

def makeBlockList(x, y, w, h):
    colorSet = set()
    for i in range(x, x+w):
        for j in range(y, y+h):
            totalColorPaper.add('%d.%d'%(i, j))
            colorSet.add('%d.%d'%(i, j))
    return colorSet

setList = []
for i in range(0, colorPaperNum):
    x1, y1, w1, h1=map(int, input().split())
    setList.append(makeBlockList(x1, y1, w1, h1))

for i in range(len(setList)-1):
    k = len(setList)-1-i
    print(len(set))
    totalColorPaper - set
    setList[i+1]-setList[i]

