import sys
from collections import deque

n = int(sys.stdin.readline())
a,b = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())
graphs = [[] for _ in range(n+1)]
visited = [-1 for _ in range(n+1)]

for _ in range(m):
  x,y = map(int, sys.stdin.readline().split())
  graphs[x].append(y)
  graphs[y].append(x)

def bfs(a):
  q = deque()
  q.append(a)
  visited[a] = 0

  while q:
    tmp = q.popleft()
    for i in graphs[tmp]:
      if visited[i] == -1:
        q.append(i)
        visited[i] = visited[tmp] + 1

bfs(a)
print(visited[b])
