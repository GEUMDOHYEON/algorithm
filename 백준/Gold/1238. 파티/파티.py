import sys
import heapq

N,M,X = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(N+1)]
INF = int(1e9)

for _ in range(M):
  s,e,t = map(int, sys.stdin.readline().split())
  graph[s].append((e,t))

def dijk(start):
  q = []
  heapq.heappush(q,(0,start))
  distance = [INF] * (N + 1)
  distance[start] = 0

  while q:
    d, now = heapq.heappop(q)

    if distance[now] < d:
      continue

    for i in graph[now]:
      if d + i[1] < distance[i[0]]:
        distance[i[0]] = d + i[1]
        heapq.heappush(q, (d + i[1], i[0]))
  return distance

result = 0
for i in range(1, N + 1):
  go = dijk(i)
  back = dijk(X)
  result = max(result, go[X] + back[i])

print(result)