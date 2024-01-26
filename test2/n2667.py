import sys

from collections import deque

N = int(sys.stdin.readline())

house = []   

for _ in range(N):
    house.append(list(map(int,sys.stdin.readline().rstrip())))

print(house)

d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(N):
    q = deque()
    q.append(house[N])
    
    while q:
        tmp = q.popleft()

        for dx, dy in d:
            
    