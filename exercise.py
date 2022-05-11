result = 0
for i in range(int(input())):
    word = input()
    print('list(word)', list(word))
    print('sorted(word, key=word.find)',sorted(word, key=word.find))
    if list(word) == sorted(word, key=word.find):
        result += 1
print(result)