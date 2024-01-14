import math

##########################################################

#### 골드바흐의 추측 문제 풀기 전에 소수 문제 공부용 #####

## 제곱근으로 소수 구하기 ##
# n = 1000
# for i in range(n):
#     c = 0
#     if i > 1:
#         for j in range(2, int(math.sqrt(i)) + 1):
#             if i % j == 0:
#                 c += 1
#         if c == 0:
#             print(i)

## 에라토스테네스의 체 ##
# n = 1000
# array = [True for i in range(n+1)]

# for i in range(2, int(math.sqrt(n) + 1)):
#     if array[i] == True:
#         j = 2
#         while i * j <= n:
#             array[i*j] = False
#             j += 1

# for i in range(2,n + 1):
#     if array[i]:
#         print(i, end=" ")

## 백준 2960 에라토스테네스의 체 ##
# c = 0

# n, k = map(int, input().split())

# array = [True for i in range(n+1)]

# for i in range(2, n+1):
#     for j in range(i,n+1,i):
#         if array[j] != False:
#             array[j] = False
#             c += 1
#             if c == k:
#                 print(j)
