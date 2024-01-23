import sys
from collections import deque

N, M = map(int,sys.stdin.readline().split())

maze = []   

for _ in range(N):
    maze.append(list(map(int,sys.stdin.readline().rstrip())))

d = [(0,-1),(0,1),(-1,0),(1,0)]

def search(y,x):
    queue = deque()
    queue.append((y,x))

    while queue:
        y,x = queue.popleft()

        for dy,dx in d:
            Y = dy + y
            X = dx + x
            if (0 <= Y < N) and (0<= X < M) and maze[Y][X] == 1:
                queue.append((Y,X))
                maze[Y][X] = maze[y][x] + 1

search(0,0)
print(maze[N-1][M-1])
