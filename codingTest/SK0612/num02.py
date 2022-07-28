def sumPayment(P):
    late12Pay = 0
    for payment in P[1:]:
        late12Pay += payment
    return late12Pay

def solution(periods, payments, estimates):
    customerN = len(periods)
    nextVIP = 0
    expiredVIP = 0
    for i in range(customerN):
        D = periods[i]
        P = payments[i]
        E = estimates[i]
        if D == 23:
            if sumPayment(P) + E>=900000:
                nextVIP += 1
                continue
        elif 23<D<59 and sum(P)<900000:
            if sumPayment(P) + E>=900000:
                nextVIP += 1
                continue
        elif D == 59 and sum(P)<900000:
            if sumPayment(P) + E>=600000:
                nextVIP += 1
                continue
        elif 59<D and sum(P)<600000:
            if sumPayment(P) + E>=600000:
                nextVIP += 1
                continue

        if 23<=D<59 and sum(P)>=900000:
            if sumPayment(P) + E<900000:
                expiredVIP += 1
                continue
        elif 59<=D and sum(P)>=600000:
            if sumPayment(P) + E<600000:
                expiredVIP += 1
                continue 
        
    return [nextVIP, expiredVIP]