# 제출만 하면 됨
# 제출 완료!

from string import ascii_lowercase
vowelList = ['a', 'e', 'i', 'o', 'u']
consoList = [a for a in list(ascii_lowercase) if a not in vowelList]

def con1(pw):
    for i in pw:
        if i in vowelList:
            return True
    return False

def con2(pw):
    tempV = []
    tempC = []
    for i in range(len(pw)-2):
        if pw[i] in vowelList:
            tempV.append(pw[i])
        else:
            tempC.append(pw[i])
        if pw[i+1] in vowelList:
            tempV.append(pw[i+1])
        else:
            tempC.append(pw[i+1])
        if len(tempV)==2 and pw[i+2] in vowelList:
            return False
        if len(tempC)==2 and pw[i+2] in consoList:
            return False
        tempV=[]
        tempC=[]
    return True

def con2_1(pw):
    if pw =='ee' or pw =='oo':
        return True
    if pw[0]==pw[1]:
        return False
    return True

def con2_2(pw):
    if pw =='ee' or pw =='oo':
        return True
    if pw[0]==pw[1]:
        return False
    return con1(pw)

def pwCheck(pw):
    if len(pw)==1:
        return con1(pw)
    if len(pw)==2:

        return con2_2(pw)
    con1Result = con1(pw)
    for i in range(len(pw)-1):
        if con2_1(pw[i:i+2])==False:
            con2Result = False
            break
        else:
            con2Result = True
    con3Result = con2(pw)
    if con1Result and con2Result and con3Result:
        return True

    return False

# houctuh
while True:
    pw = input()
    if pw == 'end':
        break
    result = 'acceptable' if pwCheck(pw) else 'not acceptable'
    print("<{0}> is {1}.".format(pw, result))
    


