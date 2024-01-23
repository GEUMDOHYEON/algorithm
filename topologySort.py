import sys

from collections import deque

N = int(sys.stdin.readline()) # 노드의 개수
M = int(sys.stdin.readline()) # 간선의 개수

graph = [[] for _ in range(N + 1)] # 인접리스트로 만든 그래프

entrance = [0] * (N + 1) # 진입 차수 개수

for i in range(1,N + 1):
    a,b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    entrance[b] += 1 

queue = deque()
for i in range(1,N + 1):
    if entrance[i] == 0:
        queue.append(i)

while queue:
    tmp = queue.popleft()
    print(tmp,end=" ")
    for i in graph[tmp]:
        entrance[i] -= 1

        if entrance[i] == 0:
            queue.append(i)
