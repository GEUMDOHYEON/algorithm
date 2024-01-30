import sys

read = sys.stdin.readline

T = int(read())

for _ in range(T):
    N = int(read())

    worker = []

    for i in range(N):
        a,b = map(int, read().split())
        worker.append([a,b])
    
    worker.sort(key=lambda x:x[0])

    count = 1
    cri = worker[0][1]

    for i in range(1,N):
        if cri > worker[i][1]:
            count += 1
            cri = worker[i][1]

    print(count)