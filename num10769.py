msg = input()

happy = msg.count(':-)')
sad = msg.count(':-(')

if happy> sad:
    print('happy')
elif happy<sad:
    print('sad')
elif happy==0 and sad==0:
    print('none')
elif happy==sad:
    print('unsure')