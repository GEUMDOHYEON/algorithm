import sys
from collections import deque

N = int(sys.stdin.readline())

zone = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(h,i,j):
    q = deque()
    
    q.append((i,j))
    visited[i][j] = 1
    count = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            n_x = x + dx[i]
            n_y = y + dy[i]

            if (0<= n_x < N) and (0<= n_y < N) and not visited[n_x][n_y]:
                if zone[n_x][n_y] > h:
                    visited[n_x][n_y] = 1
                    q.append((n_x,n_y))
    return 1

max_rain = max(map(max,zone))
reuslt = []
for h in range(max_rain):
    max_count = 0
    visited = [[0] * (N) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if zone[i][j] > h and not visited[i][j]:
                max_count += bfs(h,i,j)
    reuslt.append(max_count)

if max(reuslt) == 0:
    print(1)
else:
    print(max(reuslt))