import sys
from collections import deque

N,M = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

entrance = [0] * (N + 1)

for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    entrance[b] += 1

queue = deque()
for i in range(1,N + 1):
    if entrance[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    print(tmp, end=" ")
    for i in graph[tmp]:
        entrance[i] -= 1
        if entrance[i] == 0:
            queue.append(i)

