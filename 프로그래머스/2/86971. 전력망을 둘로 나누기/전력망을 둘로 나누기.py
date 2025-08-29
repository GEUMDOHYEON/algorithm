from collections import deque

def bfs(n, graph, visited):
    q = deque()
    q.append(n)
    visited[n] = 1
    count = 1
    
    while q:
        t = q.popleft()
        
        for i in graph[t]:
            if visited[i] == 0: 
                q.append(i)
                visited[i] = 1
                count += 1
    return count

def solution(n, wires):
    answer = n-2
    for i in range(len(wires)):
        tmps = wires.copy()
        graph = [[] for _ in range(n+1)]
        visited = [0] * (n+1)
        tmps.pop(i)
        a = []
        
        for tmp in tmps:
            v1, v2 = tmp
            graph[v1].append(v2)
            graph[v2].append(v1)
        for i in range(1, n+1):
            if visited[i] == 0:
                 a.append(bfs(i, graph, visited))
        result = abs(a[0] - a[1])
        answer = min(answer, result)
    return answer