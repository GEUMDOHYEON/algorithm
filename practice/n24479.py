import sys

sys.setrecursionlimit(10**6)

read = sys.stdin.readline

N,M,R = map(int, read().split())

graph = [[] for _ in range(N+1)]
visited = [False] * (N + 1)

for _ in range(M):
    a,b = map(int, read().split())
    graph[a].append(b)
    graph[b].append(a)

for i in graph:
    i.sort()


result = [0 for _ in range(N+1)]
count = 0
def dfs(V,E,R):
    global count
    count+=1
    visited[R] = True
    result[R] = count

    for i in graph[R]:
        if not visited[i]:
            dfs(V,E,i)

dfs(N,M,R)


for i in range(1,N+1):
    print(result[i])
