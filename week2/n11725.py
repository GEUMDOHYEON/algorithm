import sys

sys.setrecursionlimit(10**7)

N = int(sys.stdin.readline())

tree = [[] for _ in range(N+1)]

visited = [False] * (N + 1)
result = [[] for _ in range(N + 1)]

for _ in range(N-1):
    a,b = map(int,sys.stdin.readline().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(n):
    global result

    visited[n] = True

    for i in tree[n]:
        if not visited[i]:
            result[i].append(n)

            dfs(i)

dfs(1)

for i in range(2,N + 1):
    print(result[i][0])