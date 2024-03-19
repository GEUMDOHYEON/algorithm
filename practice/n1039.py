import sys
from collections import deque

read = sys.stdin.readline

N, K = map(int, read().split()) # N은 정수, K는 연산 횟수
N = list(map(str, str(N)))
M = len(N)


# def bfs(N,M):
#     q = deque(N[0])

#     while q:
#         tmp = q.popleft()
#         for i in range(M):
#             if tmp < N[i]:
                
# if M > K:
#     print(-1)
# else:
#     for i in range(K):
#         for j in range(M):  
#             if N[i] < N[j]:
#                 N[i], N[j] = N[j], N[i]
            
#     print(N)
