import sys
from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]

def bfs(x,y,c):
    q = deque()
    q.append([x,y])
    graph[x][y] = 0
    count = 0

    while q:
        t_x, t_y = q.popleft()
        count += 1
        for i in range(4):
            n_x = t_x + dx[i]
            n_y = t_y + dy[i]

            if (0<= n_x < M) and (0<= n_y < N) and (graph[n_x][n_y] == c):
                q.append([n_x,n_y])
                graph[n_x][n_y] = 0
                
    return count

N,M = map(int,sys.stdin.readline().split())

graph = []
wresult = 0
bresult = 0

for _ in range(M):
    S = list(sys.stdin.readline().strip())
    graph.append(S)

for m in range(M):
    for n in range(N):
        if graph[m][n] == 'W':
            wresult += (bfs(m,n,'W')) ** 2
        elif graph[m][n] == 'B':
            bresult += (bfs(m,n,'B')) ** 2

print(wresult,bresult)