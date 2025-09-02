def solution(players, m, k):
    answer = 0
    server = []

    for player in players:
        n = player // m
        l = len(server)
        if n != 0:
            if l == 0:
                for _ in range(n):
                    server.append(0)
                    answer += 1
            elif l > 0:
                for _ in range(n - l):
                    server.append(0)
                    answer += 1
                    
        i = 0
        while i < len(server):
            server[i] += 1
            if server[i] == k:
                server.pop(i)
            else:
                i += 1
                
                
    return answer