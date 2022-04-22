print(type('5')==str)

try: 
    int('hello')
except ValueError:
    print('here')
