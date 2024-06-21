import sys
from collections import deque

def bfs(i,j):
  q = deque()
  q.append((i,j))
  graph[i][j] = 0

  while q:
    x, y = q.popleft()

    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < h and 0<= ny < w and graph[nx][ny] == 1:
        graph[nx][ny] = 0
        q.append((nx,ny))
  return 1


while True:
  w,h = map(int,sys.stdin.readline().split())

  if w == 0 and h == 0:
    break
  
  graph = [list(map(int,sys.stdin.readline().split())) for _ in range(h)]

  dx = [1,-1,0,0,-1,-1,1,1]
  dy = [0,0,-1,1,-1,1,-1,1]

  result = 0

  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1:
        result += bfs(i,j)

  print(result)