from random import randrange
lotto = []

while len(lotto)<6:
    randNum = randrange(1, 46)
    if randNum not in lotto:
        lotto.append(randNum)
    else:
        pass
lotto.sort()
print(lotto)