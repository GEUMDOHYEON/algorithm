import sys
from collections import deque

def bfs(a,b):
  tmp = 1
  q = deque()
  q.append((a,b))
  graph[a][b] = 0

  while q:
    y, x = q.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < m and 0 <= ny < n:
        if graph[ny][nx]:
          q.append((ny,nx))
          graph[ny][nx] = 0
          tmp += 1
  return tmp

n,m = map(int, sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

dx = [0,0,-1,1]
dy = [-1,1,0,0]

result = 0
count = 0

for i in range(n):
  for j in range(m):
    if graph[i][j]:
      count += 1
      result = max(result, bfs(i,j))

print(count)
print(result)