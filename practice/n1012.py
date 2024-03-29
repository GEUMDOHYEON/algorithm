import sys
sys.setrecursionlimit(10**5)

read = sys.stdin.readline

def dfs(x,y):
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0<= nx < N) and (0<= ny < M):
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = -1
                dfs(nx,ny)
    
T = int(read())

for i in range(T):
    M,N,K = map(int, read().split())
    matrix = [[0] * M for _ in range(N)]
    count = 0

    for _ in range(K):
        x, y = map(int,read().split())
        matrix[y][x] = 1
    
    for i in range(N):
        for j in range(M):
            if matrix[i][j] > 0:
                dfs(i,j)
                count += 1
        
    print(count)
