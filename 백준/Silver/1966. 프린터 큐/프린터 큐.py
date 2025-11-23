from collections import deque

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    q = deque(list(map(int, input().split())))
    count = 0

    while q:
        best = max(q)
        tmp = q.popleft()
        M -= 1
        if best == tmp:
            count += 1
            if M < 0:
                print(count)
                break
        else:
            q.append(tmp)
            if M < 0:
                M = len(q) - 1

