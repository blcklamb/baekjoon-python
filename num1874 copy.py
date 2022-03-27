import sys

def stackPut(n, sequence):
    stack = []
    num = 1
    index = 0
    result = [] # push pop의 여부가 들어감

    while True:
        
        if len(stack) == 0:
            stack.append(num)
            result.append("+")
            num += 1
        elif sequence[index] == stack[-1]:
            stack.pop()
            result.append("-")
            index += 1
            # 전체 수를 입력된 배열처럼 담았을 때 탈출 가능
            if index == n:
                break
        else:
            # 스택에서 입력된 배열에 못 담을 때
            # 담아오는 숫자가 전체 숫자보다 큰 경우
            if n < num:
                print("NO")
                break
            stack.append(num)
            result.append("+")
            num += 1
    # 스택이 비었을 때 전체 push/pop 결과 출력
    if len(stack) == 0:
        for i in result:
            print(i)

totalNum = int(sys.stdin.readline())
numList = []
for i in range(totalNum):
    numList.append(int(sys.stdin.readline()))

stackPut(totalNum, numList)
