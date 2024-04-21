import sys
from collections import deque

N = int(sys.stdin.readline())
pic = [list(sys.stdin.readline().strip()) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
visited = [[0] * (N+1) for _ in range(N+1)]

def bfs(x,y,c):
    q = deque()
    q.append((x,y))
    visited[x][y] = 1
    
    while q:
        tx, ty = q.popleft()
        for i in range(4):
            t_x = tx + dx[i]
            t_y = ty + dy[i]
            if (0 <= t_x < N) and (0 <= t_y < N) and not visited[t_x][t_y] and pic[t_x][t_y] == c:
                visited[t_x][t_y] = 1
                q.append((t_x,t_y))
        
    return 1

result = []
r = 0
g = 0
b = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and pic[i][j] == 'R':
            r += bfs(i,j,'R')
        elif not visited[i][j] and pic[i][j] == 'G':
            g += bfs(i,j,'G')
        elif not visited[i][j] and pic[i][j] == 'B':
            b += bfs(i,j,'B')
result.append(r+g+b)

visited = [[0] * (N+1) for _ in range(N+1)]
for i in range(N):
    for j in range(N):
        if pic[i][j] == 'R':
            pic[i][j] = 'G'
g = 0
b = 0
for i in range(N):
    for j in range(N):
        if not visited[i][j] and  pic[i][j] == 'G':
            g += bfs(i,j,'G')
        elif not visited[i][j] and pic[i][j] == 'B':
            b += bfs(i,j,'B')
result.append(g+b)
for i in result:
    print(i,end=" ")