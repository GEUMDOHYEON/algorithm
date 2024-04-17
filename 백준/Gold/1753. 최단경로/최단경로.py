import sys
import heapq

INF = 10**9

def dijk(s_node):
    distane = [INF] * (V + 1)
    distane[s_node] = 0

    q = []
    heapq.heappush(q,(0,s_node))

    while q:
        w, v = heapq.heappop(q)

        if distane[v] < w:
            continue
        
        for i in graph[v]:
            # d = w + i[0]
            if distane[i[0]] > w + i[1]:
                distane[i[0]] = w + i[1]
                heapq.heappush(q,(distane[i[0]],i[0]))
    
    for i in range(1,len(distane)):
        if distane[i] == INF:
            print('INF')
            continue
        print(distane[i])



V,E = map(int,sys.stdin.readline().split())

K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)] 

for _ in range(E):
    u,v,w = map(int,sys.stdin.readline().split())
    graph[u].append([v,w])

dijk(K)
