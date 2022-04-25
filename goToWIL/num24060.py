import sys
listNum, savingNum = sys.stdin.readline().split()

# 중요!
global save_num
save_num = 0


def merge_sort(array):
	# 탈출 조건: mergeSort하는 요소가 1개가 될 때까지
    if len(array) <= 1:
        return array
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])
    print(left_array, right_array)

    return merge(left_array, right_array)

# 앞의 병합정렬 merge와 동일
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    global save_num 
    breakValue = True
    
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            save_num += 1
            if numberK(result, save_num)==-1:
                return
            array1_index += 1
        else:
            result.append(array2[array2_index])
            save_num += 1
            if numberK(result, save_num)==-1:
                return
            array2_index += 1

    if breakValue == False:
        return 

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            save_num += 1
            if numberK(result, save_num)==-1:
                return
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            save_num += 1
            if numberK(result, save_num)==-1:
                return
            array1_index += 1

    return result

global kthNum 
kthNum= 0
def numberK(array, save_num):
    global kthNum
    if save_num == savingNum:
        kthNum=array[-1]
        return -1
    else:
        pass


array = [4, 5, 1, 3, 2]
print(merge_sort(array), save_num)
print(kthNum)
