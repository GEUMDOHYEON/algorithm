from collections import deque

import sys

NODE = int(sys.stdin.readline())    # 노드의 개수
EDGE = int(sys.stdin.readline())    # 간선의 개수

count = 0   # 바이러스의 침투된 컴퓨터의 개수

graph = [[False] * (NODE + 1) for _ in range(NODE + 1)] 

for _ in range(EDGE):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (NODE + 1)  # bfs, dfs의 방문기록

# def virus(N): #dfs
#     global count
#     visited[N] = True

#     count += 1

#     for i in range(1,NODE + 1):
#         if not visited[i] and graph[N][i]:
#             virus(i)

def virus(N):   #bfs
    global count
    queue = deque()
    visited[N] = True
    queue.append(N)

    while queue:
        tmp = queue.popleft()
        count += 1
        for i in range(1, NODE+1):
            if not visited[i] and graph[tmp][i]:
                queue.append(i)
                visited[i] = True
    

virus(1)
print(count - 1)