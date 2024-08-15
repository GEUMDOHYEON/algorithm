import sys

def dfs(x,y):
  global flag
  visited[x][y] = 1

  for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if (0 <= nx < N) and (0<= ny < M):
      if maps[nx][ny] > maps[x][y]:
          flag = False
      if (visited[nx][ny] == 0) and maps[nx][ny] == maps[x][y]:
        dfs(nx,ny)

N,M = map(int,sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
visited = [[0] * (M + 1) for _ in range(N + 1)]
dx = [1,-1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,1,1,-1]
result = 0

for i in range(N):
  for j in range(M):
    if maps[i][j] > 0 and visited[i][j] == 0:
      flag = True
      dfs(i,j)
      if flag:
        result += 1

print(result)