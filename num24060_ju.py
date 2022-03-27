import sys
import math

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
cc = []


def merge_sort(A):
    a = len(A)
    if a <= 1:
        return A
    aa = merge_sort(A[:math.ceil(a / 2)])
    bb = merge_sort(A[math.ceil(a / 2):])
    return merge(aa, bb)


def merge(aa, bb):
    tmp = []
    global cc
    while len(aa) != 0 and len(bb) != 0:
        if aa[0] < bb[0]:
            tmp.append(aa.pop(0))
        else:
            tmp.append(bb.pop(0))
    while len(aa) != 0:
        tmp.append(aa.pop(0))
    while len(bb) != 0:
        tmp.append(bb.pop(0))
    cc += tmp
    return tmp


merge_sort(A)
if len(cc) < K:
    print(-1)
else:
    print(cc[K - 1])
