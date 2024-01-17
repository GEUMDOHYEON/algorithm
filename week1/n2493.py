import sys

N = int(sys.stdin.readline())

towers = list(map(int, sys.stdin.readline().split()))
stack = []
result = []

for i in range(N):
    while stack:
        if stack[-1][1] >= towers[i]:
            result.append(stack[-1][0] + 1)
            break
        else:
            stack.pop()
        
    if not stack:
        result.append(0)

    stack.append((i,towers[i]))

# 시간 초과 나옴. 
# while towers:
#     tmp = towers.pop()
#     count = 0
#     idx = len(towers)
#     for i in range(len(towers)-1,-1,-1):
#         if tmp < towers[i]:
#             result.append(i+1)
#             break
#         else:
#             count += 1
        
#         if count == idx:
#             result.append(0)

# result.append(0)

# result.reverse()

for i in result:
    print(i,end=" ")
