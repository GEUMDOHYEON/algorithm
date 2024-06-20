import sys
from collections import deque

read = sys.stdin.readline

def dfs(n):
    q = deque([n])

    while q:
        tmp = q.popleft()
        if tmp == K:
            print(graph[tmp])
            break
        for i in (tmp-1,tmp+1,tmp*2):
            if 0 <= i <= MAX and not graph[i]:
                graph[i] = graph[tmp] + 1
                q.append(i)
                
N, K = map(int,read().split())
MAX = 10**5
graph = [0] * (MAX + 1)

dfs(N)
