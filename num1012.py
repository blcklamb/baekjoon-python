import sys

testCase = sys.stdin.readline()

def checkIfAdjac(list, spot):
  minusNum = 0
  spotX = spot[0]
  spotY = spot[1]
  for i in list:
      if i[0] == spotX:
          if i[1] - 1 == spotY:
            minusNum += 1
          elif i[1] + 1 == spotY:
            minusNum += 1
      elif i[1] == spotY:
          if i[0] - 1 == spotX:
            minusNum += 1
          elif i[0] + 1 == spotX:
            minusNum += 1
  return minusNum


for i in range(int(testCase)):
  bM, bN, bNum = map(int, sys.stdin.readline().split())
  bwwNum = bNum
  bList = []
  while len(bList) < bNum:
      bSpotX, bSpotY = map(int, sys.stdin.readline().split())
      if len(bList) > 0:
        bwwNum -= checkIfAdjac(bList, (bSpotX, bSpotY))
      bList.append((bSpotX, bSpotY))
  print(bwwNum)