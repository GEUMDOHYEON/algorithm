import sys
from collections import deque
read = sys.stdin.readline

N, M = map(int,read().split())

matrix = [list(map(int,read().split())) for _ in range(N)]

def bfs(x,y):
    matrix[x][y] = 0
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    w = 1
    q = deque()
    q.append([x,y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if (0<= nx < N) and (0 <= ny < M) and matrix[nx][ny]:
                q.append([nx,ny])
                matrix[nx][ny] = 0
                w +=1
    return w

count = 0
big_pic = 0
for i in range(N):
    for j in range(M):
        if matrix[i][j]:
            count += 1
            big_pic = max(bfs(i,j),big_pic)
    
    
print(count)
print(big_pic)
