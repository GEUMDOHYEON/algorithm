import sys, copy
from collections import deque
from itertools import combinations

N,M = map(int, sys.stdin.readline().split())

graph = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
answer = 0
empty = []
for i in range(N):
    for j in range(M):
        if graph[i][j] == 0:
            empty.append((i,j))

def bfs():
    global answer
    
    for c in combinations(empty,3): # 3개의 벽 세울 수 있는 모든 경우의 수
        n_graph = copy.deepcopy(graph) # 원래 그래프 보존

        for i in c: # 새로운 벽 세우기
            n_graph[i[0]][i[1]] = 1

        virus = deque()
        for i in range(N):
            for j in range(M):
                if n_graph[i][j] == 2:
                    virus.append((i,j))

        while virus:
            t_x, t_y = virus.popleft()
            for i in range(4):
                n_x = t_x + dx[i]
                n_y = t_y + dy[i]

                if (0<= n_x < N) and (0<= n_y < M) and (n_graph[n_x][n_y] == 0):
                    n_graph[n_x][n_y] = 2
                    virus.append((n_x,n_y))
        count = 0
        for i in range(N):
            for j in range(M): 
                if n_graph[i][j] == 0:
                    count += 1

        answer = max(answer,count)
bfs()
print(answer)