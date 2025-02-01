import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
visited = [[-1] * (m) for _ in range(n)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(a,b):
  q = deque()
  q.append((a, b))
  visited[a][b] = 0

  while q:
    y, x = q.popleft()
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < m and 0 <= ny < n and visited[ny][nx] == -1:
        if maps[ny][nx] == 0:
          visited[ny][nx] = 0
        elif maps[ny][nx] == 1:
          q.append((ny, nx))
          visited[ny][nx] = visited[y][x] + 1

for i in range(n):
  for j in range(m):
    if maps[i][j] == 2 and visited[i][j] == -1:
      bfs(i, j)

for i in range(n):
  for j in range(m):
    if maps[i][j] == 0:
      print(0, end=" ")
    else:
      print(visited[i][j], end=" ")
  print()