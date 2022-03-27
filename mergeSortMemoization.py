import math

memo = {
    1 : 0,
    2 : 2,
    3 : 5
}

def mergeSortCount(n, msMemo):
    if n in msMemo:
        return msMemo[n]
    nthMemo = mergeSortCount(math.ceil(n/2), msMemo) + mergeSortCount(n-math.ceil(n/2), msMemo) + n
    memo[n] = nthMemo
    return nthMemo

print(mergeSortCount(100, memo))