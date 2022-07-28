def solution(n, plans, clients):
    answer = []
    plansData=[]
    plansService=[]
    clientsData = []
    clientsService = []

    for i in plans:
        infoList = list(map(int, i.split()))
        plansData.append(infoList[0])
        if i != plans[0]:
            plansService.append(plansService[-1]+(infoList[1:]))
        else:
            plansService.append((infoList[1:]))
    for i in clients:
        infoList = list(map(int, i.split()))
        clientsData.append(infoList[0])
        clientsService.append((infoList[1:]))

    clientsNum = len(clients)
    plansNum = len(plans)


    for i in range(clientsNum):
        for j in range(plansNum):
            if len(list(set(clientsService[i]) | set(plansService[j])))<=len(plansService[j]):
                if clientsData[i]<=plansData[j]:
                    answer.append(j+1)
                    break
                continue
        if len(answer) != i+1:
            answer.append(0)
    return answer