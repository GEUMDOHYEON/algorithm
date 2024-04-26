from collections import deque

A, B = map(int,input().split())
count = 0
q = deque()
q.append((A,1))

while q:
    n,t = q.popleft()

    if n > B:
        continue
    if n == B:
        print(t)
        break
    q.append((2*n,t+1))
    q.append((int(str(n) + str(1)), t+1 ))
    
else:
    print(-1)