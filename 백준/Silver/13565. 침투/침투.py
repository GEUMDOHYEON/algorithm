import sys
from collections import deque

def bfs(y,x):
  q = deque()

  q.append((y,x))
  graph[y][x] = 2
  while q:
    y,x = q.popleft()

    for i in range(4):
      n_x = x + dx[i]
      n_y = y + dy[i]

      if 0 <= n_x < N and 0 <= n_y < M and graph[n_y][n_x] == 0:
        q.append((n_y,n_x))
        graph[n_y][n_x] = 2

M,N = map(int,sys.stdin.readline().split())
dx = [0,0,-1,1]
dy = [1,-1,0,0]

graph = [list(map(int,sys.stdin.readline().strip())) for _ in range(M)]

for i in range(N):
  if graph[0][i] == 0:
    bfs(0,i)

print("YES" if 2 in graph[-1] else "NO")