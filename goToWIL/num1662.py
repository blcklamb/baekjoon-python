# 메모리초과
'''
str = input()
stack = []

for i in str:
    strLength = 0
    if i==')':
        strIndex=0
        zipNum = ''
        while True:
            temp = stack.pop()
            if temp=='(':
                num = stack.pop()
                strLength += int(num)*len(zipNum)
                stack.append('1'*strLength)
                break
            zipNum += temp
            strIndex+=1
    else:
        stack.append(i)

answer = 0
for i in stack:
    if i == '':
        pass
    else:
        answer += len(i)
print(answer)
'''
# 참고 https://namhandong.tistory.com/140
str = input()
stack = []
length = 0
temp = ''

for i in str:
    if i == '(':
        stack.append((temp, length-1))
        length = 0
    elif i == ')':
        zippedNum, preLength = stack.pop()
        length = (int(zippedNum)*length)+preLength
    else:
        length += 1
        temp = i

print(length)

# 우수 코드
s=[]
f=lambda t:[t,1][type(t)==str]
for i in input():
    if i==')':
        l,t=0,s.pop()
        while t!='(':l+=f(t);t=s.pop()
        s+=[int(s.pop())*l]
    else:s+=[i]
print(sum(map(f,s)))