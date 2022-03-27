import math
import sys

N, K = map(int, sys.stdin.readline().strip().split(' '))
A = list(map(int, sys.stdin.readline().strip().split(' ')))
count = 0

def mergeSort(array):
    def merge(arr1, arr2):
        result = []
        arr1_index = 0
        arr2_index = 0
        global N, K
        global count
        # 두 리스트 길이에 모두 도달하지 않았을 때
        while arr1_index < len(arr1) and arr2_index < len(arr2):
            if arr1[arr1_index] < arr2[arr2_index]:
                result.append(arr1[arr1_index])
                arr1_index += 1
            else:
                result.append(arr2[arr2_index])
                arr2_index += 1
            count += 1
            if count == K:
                print(result[-1])
        # 한 개의 리스트를 먼저 다 넣었을 때
        if arr1_index == len(arr1):
            while arr2_index != len(arr2):
                result.append(arr2[arr2_index])
                arr2_index += 1
                count += 1
                if count == K:
                    print(result[-1])
        if arr2_index == len(arr2):
            while arr1_index != len(arr1):
                result.append(arr1[arr1_index])
                arr1_index += 1
                count += 1
                if count == K:
                    print(result[-1])
        # N개를 다 합했지만 count가 K보다 작을 때
        if len(result) == N:
            if count < K:
                print(-1)

        return result

    if len(array) <= 1:
        return array # 최종 원소 하나짜리 배열
    mid = math.ceil(len(array)/2)
    # 재귀 사용
    first_array = mergeSort(array[:mid])
    second_array = mergeSort(array[mid:])

    return merge(first_array, second_array)

mergeSort(A)