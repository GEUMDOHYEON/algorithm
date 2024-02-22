# import heapq
# import sys
# read = sys.stdin.readline

# a = [10,9,5,8,3,2,4,6,7,1]
# heapq.heapify(a)
# # print(a)
# for i in a:
#     # heapq.heappush(a[:len(a)-i],i)
#     heapq.heappop(a)
#     print(a)

##########################################
## 최소 힙 ##

# N = int(read())
# x = []
# heapq.heapify(x)

# for i in range(N):
#     a = int(read())
#     if a != 0:
#         heapq.heappush(x,a) 
#     if a == 0:
#         if len(x) == 0:
#             print(0)
#         else:
#             tmp = heapq.heappop(x)
#             print(tmp)



###########################################
## 최소 힙을 이용한 힙정렬 ##

# N,M = map(int,read().split())

# array = list(map(int,read().split()))
# result = []

# for i in range(len(array)):
#     heapq.heapify(array)
#     result.append(heapq.heappop(array))

# print(result)