import sys
from collections import deque

m,n,k = map(int, sys.stdin.readline().split())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
graphs = [[0] * n for _ in range(m)]
visited = [[0] * n for _ in range(m)]
result = []

for _ in range(k):
  lx, ly, rx, ry = map(int, sys.stdin.readline().split())
  for i in range(lx, rx):
    for j in range(ly, ry):
      graphs[j][i] = 1

def bfs(a,b):
  q = deque()
  q.append((a,b))
  visited[a][b] = 1
  count = 1

  while q:
    x,y = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n and visited[nx][ny] == 0 and graphs[nx][ny] == 0:
        q.append((nx,ny))
        visited[nx][ny] = 1
        count += 1
  return count

for i in range(m):
  for j in range(n):
    if graphs[i][j] == 0 and visited[i][j] == 0:
      result.append(bfs(i,j))

result.sort()
print(len(result))
for a in result:
  print(a, end=" ")