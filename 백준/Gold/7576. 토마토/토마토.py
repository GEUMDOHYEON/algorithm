import sys
from collections import deque

M,N = map(int,sys.stdin.readline().split())
tomato = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
q = deque()

for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            q.append((i,j))

def bfs():
    while q:
        tx, ty = q.popleft()
        for i in range(4):
            t_x = tx + dx[i]
            t_y = ty + dy[i]
            if (0<= t_x <N) and (0<= t_y <M) and tomato[t_x][t_y] == 0:
                tomato[t_x][t_y] = tomato[tx][ty] + 1
                q.append((t_x,t_y))

bfs()
result = 0

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    result = max(result,max(i))
print(result-1)