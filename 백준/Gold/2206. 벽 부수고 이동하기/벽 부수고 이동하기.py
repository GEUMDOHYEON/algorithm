import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

visited = [[[0,0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
dx = [0,0,-1,1]
dy = [-1,1,0,0]

def bfs(x,y):
  q = deque()
  q.append((x,y,0))
  
  while q:
    x,y,z = q.popleft()

    if x == N - 1 and y == M - 1:
      return visited[x][y][z]
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < N and 0 <= ny < M:
        if maps[nx][ny] == 1 and z == 0:
          visited[nx][ny][1] = visited[x][y][0] + 1
          q.append((nx,ny,1))
        if maps[nx][ny] == 0 and visited[nx][ny][z] == 0:
          visited[nx][ny][z] = visited[x][y][z] + 1
          q.append((nx,ny,z))

  return -1

print(bfs(0,0))