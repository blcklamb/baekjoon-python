import sys
sgCards = int(input())
sgCardNum = list(map(int, sys.stdin.readline().split()))
guessCards = int(input())
guessCardNum = list(map(int, sys.stdin.readline().split()))
howmanyStr=''
for guessnum in guessCardNum:
    if guessnum in sgCardNum:
        howmany=sgCardNum.count(guessnum)
    else:
        howmany=0
    howmanyStr += ' ' + str(howmany)
print(howmanyStr.lstrip())