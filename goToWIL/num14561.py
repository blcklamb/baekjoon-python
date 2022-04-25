# 10진법 수num을 base진법으로 변환 
def tenToNbase(num, base):
    toNbase = []
    while num > 0:
        num, mod = divmod(num, base) #base로 나눈 몫과 나머지
        toNbase.append(str(mod)) #나머지는 차례대로 붙이기
    return toNbase[::-1]

#회문인지 판별
def isPalindrome(num, base):
    numBase=str(tenToNbase(int(num), int(base)))
    for i in range(0, len(numBase)//2): #숫자 문자열을 반으로 나누어
        if numBase[i]!=numBase[len(numBase)-1-i]: #한쪽이 끝쪽과 같은지 판별
            return 0 #하나라도 다르면 0 회문 아님
    return 1

num = int(input())
resultList = []
for i in range(num):
    inputCase=input().split()
    resultList.append(isPalindrome(inputCase[0], inputCase[1]))

print(*resultList, sep='\n')

# https://velog.io/@code_angler/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A7%84%EC%88%98%EB%B3%80%ED%99%982%EC%A7%84%EB%B2%95-3%EC%A7%84%EB%B2%95-5%EC%A7%84%EB%B2%95-10%EC%A7%84%EB%B2%95n%EC%A7%84%EB%B2%95