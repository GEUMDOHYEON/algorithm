import sys

sys.setrecursionlimit(10**6)

K = int(sys.stdin.readline())

def dfs(start,visited,graph,group):
    visited[start] = group

    for i in graph[start]:
        if visited[i] == 0:
            result = dfs(i,visited,graph,-group)
            if not result:
                return False
        else:
            if visited[i] == group:
                return False
    return True


for _ in range(K):
    V, E = map(int,sys.stdin.readline().split())

    graph = [[] for _ in range(V + 1)]

    visited = [0] * (V + 1)

    for _ in range(E):
        a,b = map(int,sys.stdin.readline().split())
        graph[a].append(b)
        graph[b].append(a)

    for i in range(1,V + 1):
        if visited[i] == 0:
            result = dfs(i,visited,graph,1)
            if not result:
                break
    print("YES") if result else print("NO")

