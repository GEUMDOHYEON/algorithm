import sys

N,M = map(int,sys.stdin.readline().split())

floor = []

for i in range(N):
    floor.append(list(input()))

count = 0

def dfs(x,y):
    global count
    
    dx = x + 1
    dy = y + 1

    if x == N or y == M:
        count += 1
        return

    if floor[x][y] == '-':
        if dy < M and floor[x][dy] == '|':
            count += 1
            return
        if dy == M:
            count += 1

    if floor[x][y] == '|':
        if dx < N and floor[dx][y] == '-':
            count += 1
            return
        if dx == N:
            count += 1

for i in range(N):
    for j in range(M):
        if floor[i][j] == '-':
            dfs(i,j)
            
        if floor[i][j] == '|':
            dfs(i,j)    

print(count)
