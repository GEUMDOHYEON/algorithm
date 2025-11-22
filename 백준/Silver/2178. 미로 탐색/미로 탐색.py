from collections import deque

N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
visited = [[False for _ in range(M)] for _ in range(N)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def BFS():
  q = deque()
  q.append((0,0,1))
  visited[0][0] = True

  while q:
    x,y,cnt = q.popleft()

    if x == N-1 and y == M-1:
      return cnt
    
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and maze[nx][ny] == 1:
        q.append((nx,ny,cnt + 1))
        visited[nx][ny] = True

print(BFS())
