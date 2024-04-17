import sys

N,M = map(int,sys.stdin.readline().split())

island = []

for _ in range(N):
    S = list(sys.stdin.readline().strip())
    island.append(S)

x,y = 0,0

for i in range(N):
    for j in range(M):
        if 'R' == island[i][j]:
            x, y = i, j

dp = [[-1] * M for _ in range(N)]
dp[x][y] = 0
dx = [-1,0,1]
dy = [-1,-1,-1]

def search(r,c):
    if (0<= r < N) and (0<= c < M):
        return True
    return False

flag = 0 
count = 0

for j in range(y+1,M):
    for i in range(0,N):
        if island[i][j] == '#':
            continue
        for _ in range(3):
            n_x = i + dx[_]
            n_y = j + dy[_]
            if search(n_x,n_y) and dp[n_x][n_y] != -1:
                if island[i][j] == 'C':
                    dp[i][j] = max(dp[i][j], dp[n_x][n_y] + 1)
                if island[i][j] == '.':
                    dp[i][j] = max(dp[i][j], dp[n_x][n_y])
                if island[i][j] == 'O':
                    flag = 1
                    dp[i][j] = max(dp[i][j], dp[n_x][n_y])
                    count = max(count, dp[i][j])
if flag:
    print(count)
else:
    print(-1)