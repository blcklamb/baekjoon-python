#시간 초과
# orderNum = int(input())
# stack = []
# for _ in range(orderNum):
#     orders = input()
#     if 'push' in orders:
#         orders, value = orders.split()
#     if orders == 'push':
#         stack.append(int(value))
#     elif orders == 'pop':
#         print(stack.pop()) if stack else print(-1)
#     elif orders == 'size':
#         print(len(stack))
#     elif orders == 'empty':
#         print(1) if len(stack)==0 else print(0)
#     else:
#         print(-1) if stack == [] else print(stack[-1])

# sys.stdin.readline 쓰니깐 해결
import sys
orderNum = int(sys.stdin.readline())
stack = []
for _ in range(orderNum):
    orders = sys.stdin.readline().strip()
    if 'push' in orders:
        orders, value = orders.split()
    if orders == 'push':
        stack.append(int(value))
    elif orders == 'pop':
        print(stack.pop()) if stack else print(-1)
    elif orders == 'size':
        print(len(stack))
    elif orders == 'empty':
        print(1) if len(stack)==0 else print(0)
    else:
        print(-1) if stack == [] else print(stack[-1])