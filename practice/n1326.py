import sys

from collections import deque 

read = sys.stdin.readline

N = int(read())

bridge = list(map(int,read().split()))
a,b = map(int,read().split())

visited = [-1] * N

def bfs(start,finish, n, bridge):
    q = deque([start - 1])
    visited[start - 1] = 0
    while q:
        tmp = q.popleft()
        for i in range(tmp, n, bridge[tmp]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[tmp] + 1
                if i == finish - 1:
                    return visited[i]
        for i in range(tmp, -1, -bridge[tmp]):
            if visited[i] == -1:
                q.append(i)
                visited[i] = visited[tmp] + 1
                if i == finish - 1:
                    return visited[i]
    return -1

answer = bfs(a,b,N,bridge)
print(answer)