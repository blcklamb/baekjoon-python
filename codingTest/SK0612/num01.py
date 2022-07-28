def solution(p):
    
    n = len(p)

    answer = [0]*n

    answerP = [i for i in range(1, n+1)]
    
    for i in range(n-1):
        if p[i] == i+1:
            answer[i] = 0
        else:
            for j in range(i+1, n):
                if p[j] == i+1:
                    p[j] = p[i]
                    p[i] = i+1
                    answer[i] += 1
                    answer[j] += 1
                    break 
        if p==answerP:
            break
            
    return answer