vowelList = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']
while True:
    inputStr = input()
    if inputStr == '#':
        break
    count = 0
    for i in inputStr:
        if i in vowelList:
            count += 1
    print(count)