from collections import deque

T = int(input())
dx = [-2,-1,-2,-1,1,2,2,1]
dy = [-1,-2,1,2,-2,-1,1,2]

def bfs(a,b):
  q = deque([(a, b, 0)])
  visited[a][b] = True

  while q:
    x, y, count = q.popleft()
    
    if x == end_x and y == end_y:
      return count
    
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]
      if 0 <= nx < l and 0 <= ny < l and not visited[nx][ny]:
        q.append([nx, ny, count + 1])
        visited[nx][ny] = True

for _ in range(T):
  l = int(input())
  start_x, start_y = map(int, input().split())
  end_x, end_y = map(int, input().split())
  graph = [[0] * l for _ in range(l)]
  visited = [[False] * l for _ in range(l)]
  print(bfs(start_x, start_y))
    
