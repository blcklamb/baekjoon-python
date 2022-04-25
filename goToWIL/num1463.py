N = int(input())

def minOpe(num):
    
    T = [0 for _ in range(num+4)]
    T[1] = 0
    T[2] = 1
    T[3] = 1

    for i in range(4, num+4):
        T[i] = T[i-1]+1
        if i%2==0:
            T[i] = min(T[i], T[i//2]+1)
        if i%3==0:
            T[i] = min(T[i], T[i//3]+1)
    
    return T[num]

print(minOpe(N))
