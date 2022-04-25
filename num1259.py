# 0409
# 숏코딩으로 도전해볼까...?

def isPalindrome(num):
    if len(num)%2==0:
        temp01 = num[:len(num)//2]
        temp02 = num[len(num)//2:]
    else:
        if len(num)==1:
            return True
        temp01 = num[:len(num)//2]
        temp02 = num[(len(num)//2)+1:]
    if temp01 == temp02[::-1]:
        return True
    else: 
        return False

while True:
    num = input()
    if num == '0':
        break
    if isPalindrome(num):
        print("yes")
    else:
        print("no")
