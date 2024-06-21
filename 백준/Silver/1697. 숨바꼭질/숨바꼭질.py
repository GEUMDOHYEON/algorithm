import sys
from collections import deque

def bfs(n):
  q = deque()
  q.append(n)

  while q:
    a = q.popleft()
    if a == K:
      print(time[a])
      break
    for i in (a-1,a+1,a*2):
      if 0<= i < 100001 and not time[i]:
        time[i] = time[a] + 1
        q.append(i)


N,K = map(int,sys.stdin.readline().split())
time = [0] * 100001

bfs(N)
