import sys
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    apart[x][y] = 0
    count = 1

    while q:
        nx,ny = q.popleft()

        for i in range(4):
            n_x = nx + dx[i]
            n_y = ny + dy[i]

            if 0 <= n_x < N and 0 <= n_y < N and apart[n_x][n_y] == 1:
                apart[n_x][n_y] = 0
                count += 1
                q.append((n_x,n_y))

    return count

N = int(sys.stdin.readline())
apart = [list(map(int, input())) for _ in range(N)]
dx = [1,-1,0,0]
dy = [0,0,-1,1]
result = []

for i in range(N):
    for j in range(N):
        if apart[i][j] == 1:
            result.append(bfs(i,j))

print(len(result))
result.sort()
for i in result:
    print(i)