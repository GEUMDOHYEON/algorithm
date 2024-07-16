import sys
from collections import deque

N = int(sys.stdin.readline())

graph = [[] for _ in range(N+1)]
result = []

for i in range(N):
  n = int(sys.stdin.readline())
  graph[n].append(i+1)

def dfs(n):
  visited = [0] * (N + 1)
  q = deque()
  q.append(n)
  visited[n] = 1

  while q:
    tmp = q.pop()

    for i in graph[tmp]:
      if not visited[i]:
        q.append(i)
        visited[i] = 1
      elif visited[i] and i == n:
        result.append(i)

for i in range(1,N+1):
  dfs(i)

result.sort()
print(len(result))
for i in result:
  print(i)