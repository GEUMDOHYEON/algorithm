import sys
from collections import deque

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graphs = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for i in range(m):
  a,b = map(int, sys.stdin.readline().split())
  graphs[a].append(b)
  graphs[b].append(a)

def bfs():
  q = deque()
  q.append(1)
  visited[1] = 1

  while q:
    a = q.popleft()
    for i in graphs[a]:
      if visited[i] == 0:
        q.append(i)
        visited[i] = visited[a] + 1

bfs()
result = 0
for i in range(2,n+1):
  if visited[i] < 4 and visited[i] != 0:
    result += 1

print(result)