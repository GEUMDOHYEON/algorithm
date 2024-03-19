from collections import deque

import sys

N, M, V = map(int,sys.stdin.readline().split())

# graph = [[False] * (N + 1) for _ in range(N + 1)]
graph = [[] for _ in range(N + 1)]

# for _ in range(M):
#     a, b = map(int, input().split())
#     graph[a][b] = True
#     graph[b][a] = True

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    # graph[b][a] = True

visited1 = [False] * (N + 1)  # dfs의 방문기록
visited2 = [False] * (N + 1)  # bfs의 방문기록

def dsf(V):     #dsf를 구현한 재귀함수 (인접 리스트)
    visited1[V] = True # 재방문하지 않기 위해 visited1[V]에 True 대입
    print(V,end=" ")

    for i in graph[V]:
        if not visited1[i]:  
            dsf(i)

def bsf(V):
    queue = deque()
    visited2[V] = True 
    queue.append(V)

    while queue:
        V = queue.popleft()
        print(V,end=" ")
        for i in graph[V]:
            if not visited2[i]:
                queue.append(i)
                visited2[i] = True

dsf(V)
print()
bsf(V)

# def dsf(V):     #dsf를 구현한 재귀함수 (인접 행렬)
#     visited1[V] = True # 재방문하지 않기 위해 visited1[V]에 True 대입
#     print(V,end=" ")

#     for i in range(1,N+1):
#         if not visited1[i] and graph[V][i]:  
#             dsf(i)

# def bsf(V):       # 인접 행렬로 구현한 bsf
#     queue = deque()
#     visited2[V] = True 
#     queue.append(V)

#     while queue:
#         V = queue.popleft()
#         print(V,end=" ")
#         for i in range(1,N+1):
#             if not visited2[i] and graph[V][i]:
#                 queue.append(i)
#                 visited2[i] = True
