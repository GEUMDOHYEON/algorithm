import sys
import heapq

T = int(sys.stdin.readline())

for _ in range(T):
    N, K = map(int, sys.stdin.readline().split())

    time = list(map(int, sys.stdin.readline().split()))
    time.insert(0,0)
    graph = [[] for i in range(N+1)]
    indegree = [0] * (N + 1)

    for i in range(K):
        x, y = map(int, sys.stdin.readline().split())
        graph[x].append(y)
        indegree[y] += 1

    W = int(sys.stdin.readline())

    q = []
    count = 0
    result = [0] * (N+1)

    for i in range(1,len(indegree)):
        if indegree[i] == 0:
            heapq.heappush(q,[0,i])

    while q:
        count = 0
        s_node,a_node = heapq.heappop(q)
        count = time[a_node] + result[s_node]
        result[a_node] = max(count, result[a_node])
        # print(indegree)
        
        for i in graph[a_node]:
            indegree[i] -= 1
            if indegree[i] == 0:
                heapq.heappush(q,[a_node,i])
            result[i] = max(time[i]+result[a_node],result[i])
    print(result[W])
