import sys
from collections import deque   

read = sys.stdin.readline

def bfs():
    q = deque()
    q.append([home[0],home[1]])

    while q:
        x,y = q.popleft()
        if abs(x - rock[0]) + abs(y-rock[1]) <= 1000:
            print("happy")
            return
        for i in range(n):
            new_x, new_y = store[i]
            if abs(x - new_x) + abs(y - new_y) <= 1000:
                if not visited[i]:
                    q.append([new_x,new_y])
                    visited[i] = 1
          
    print("sad")
    return    


t = int(read())

for i in range(t):
    n = int(read())
    home = list(map(int,read().split())) 

    store = []
    for _ in range(n):
        x, y = map(int,read().split())
        store.append([x,y]) 

    rock = list(map(int, read().split()))

    visited = [0 for _ in range(n+1)]
    bfs()
