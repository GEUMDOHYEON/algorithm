import sys
from collections import deque

read = sys.stdin.readline

N, M = map(int, read().split())

graph = [[] for _ in range(N + 1)]

for _ in range(M):
    A,B = map(int, read().split())
    graph[B].append(A)


def bfs(v):
    q = deque([v])
    visited = [False] * (N + 1)
    visited[v] = True
    count = 1
    while q:
        tmp = q.popleft()
        for i in graph[tmp]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
                count += 1

    return count


result = []
for i in range(1,N + 1):
    result.append(bfs(i))

max_result = max(result)
for i in range(len(result)):
    if max_result == result[i]:
        print(i+1, end=" ")




#############################################
# result = [0] * (N + 1)

# def dfs(V):
#     visited = [False] * (N + 1)

#     visited[V] = True
    
#     for i in graph[V]:
#         result[i] += 1
#         if not visited[i]:
#             dfs(i)

# dfs(1)

# print(result)
# for i in range(len(result)):
#     if max(result) == result[i]:
#         print(i, end=" ")
