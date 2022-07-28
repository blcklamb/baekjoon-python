'''
nums = [1, 2, 3, -4, -5, 3]

# def sqsum1():
# 	return sum(x**2 if x > 0 for x in nums)

def sqsum2():
  	return sum(x^2 for x in nums if x > 0)

# def sqsum3():
#   	return sum(for x in nums if x > 0 then x^2)

def sqsum4():
  	return sum(x**2 for x in nums if x > 0)

# def sqsum5():
#   	return sum(x^2 if x > 0 for x in nums)

# print(sqsum1())
print(sqsum2())
# print(sqsum3())
print(sqsum4())
# print(sqsum5())
'''
import time

def f1(list_of_list):
    result = []
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in result:
                result.append(x)
    return result

def f2(list_of_list):
    flat_list = []
    for inner_list in list_of_list:
        flat_list.extend(inner_list)
    return [
        x for i, x in enumerate(flat_list)
        if flat_list.index(x) == i]

def f3(list_of_list):
    result = []
    seen = set()
    for inner_list in list_of_list:
        for x in inner_list:
            if x not in seen:
                result.append(x)
                seen.add(x)
    return result

list_of_list = [[1, 2, 3, 4]]

start_time = time.time()
f1(list_of_list)
print(time.time() - start_time)

start_time2 = time.time()
f2(list_of_list)
print(time.time()-start_time2)

start_time3 = time.time()
f3(list_of_list)
print(time.time()-start_time3)