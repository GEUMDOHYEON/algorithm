import sys

NODE = int(sys.stdin.readline())
EDGE = int(sys.stdin.readline())

count = 0

graph = [[False] * (NODE + 1) for _ in range(NODE + 1)]

for _ in range(EDGE):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited = [False] * (NODE + 1)  # dfs의 방문기록

def virus(N):
    global count
    visited[N] = True
    # print(N,end=" ")

    count += 1

    for i in range(1,NODE + 1):
        if not visited[i] and graph[N][i]:
            virus(i)


virus(1)
print(count - 1)