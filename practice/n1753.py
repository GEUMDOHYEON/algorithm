import sys
import heapq

INF = 10**9

V,E = map(int,sys.stdin.readline().split())

K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)] 

distane = [INF] * (V + 1)

def dijk(s_node):
    distane[s_node] = 0
    q = []
    heapq.heappush(q,(0,s_node))

    while q:
        w, v = heapq.heappop(q)

        if distane[v] < w:
            continue
        
        for i in graph[v]:
            if distane[i[0]] > w + i[1]:
                distane[i[0]] = w + i[1]
                heapq.heappush(q,(distane[i[0]],i[0]))

for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])

dijk(K)

for i in range(1,V+1):
    if distane[i] == INF:
        print('INF')
    else:
        print(distane[i])