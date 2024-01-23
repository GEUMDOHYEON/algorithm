import sys 

from collections import deque

INF = int(1e+9)

N,M,K,X = map(int, sys.stdin.readline().split()) 

graph = [[False] * (N + 1) for _ in range(N + 1)]
graph = [[]  for _ in range(N + 1)]

visited = [False] * (N + 1)
distance = [INF] * (N + 1)
distance[X] = 0

for _ in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    # graph[b].append(a)

queue = deque()
queue.append(X)

while queue:
    tmp = queue.popleft()

    for next in graph[tmp]:
        if distance[next] == INF:
            distance[next] = distance[tmp] + 1
            queue.append(next)

check = False

for i in range(1, N+1):
    if distance[i] == K:
        print(i)
        check = True

if check == False:
    print(-1)


### 인접 행렬로 푼 코드 --> 메모리 초과 -> 인접리스트로 풀어야됨!
# for i in range(M):
#     a,b = map(int, sys.stdin.readline().split())
#     graph[a][b] = True
#     graph[b][a] = True

# queue = deque()
# queue.append(X)
# visited[X] = True

# while queue:
#     tmp = queue.popleft()

#     for i in range(1, N+1):
#         if graph[tmp][i] and distance[tmp] + 1 < distance[i]:
#             distance[i] = distance[tmp] + 1

#         if not visited[i] and graph[tmp][i]:
#             queue.append(i)
#             # visited[i] = True

