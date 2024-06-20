import sys
from collections import deque

def bfs():
    while f_time:
        x, y = f_time.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C and maze[nx][ny] != '#' and f_visited[nx][ny] == -1:
                f_visited[nx][ny] = f_visited[x][y] + 1
                f_time.append((nx, ny))
    
    while j_time:
        x, y = j_time.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < R and 0 <= ny < C:
                if maze[nx][ny] != '#' and j_visited[nx][ny] == -1:
                    if f_visited[nx][ny] == -1 or f_visited[nx][ny] > j_visited[x][y] + 1:
                        j_visited[nx][ny] = j_visited[x][y] + 1
                        j_time.append((nx, ny))
            else:
                return j_visited[x][y] + 1
    
    return 'IMPOSSIBLE'

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

R, C = map(int, sys.stdin.readline().split())
maze = [list(sys.stdin.readline().strip()) for _ in range(R)]

j_time = deque()
f_time = deque()

j_visited = [[-1] * C for _ in range(R)]
f_visited = [[-1] * C for _ in range(R)]

for i in range(R):
    for j in range(C):
        if maze[i][j] == 'F':
            f_time.append((i, j))
            f_visited[i][j] = 0
        elif maze[i][j] == 'J':
            j_time.append((i, j))
            j_visited[i][j] = 0

print(bfs())
