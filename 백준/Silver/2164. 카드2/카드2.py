from collections import deque

I = int(input())

q = deque()

for i in range(1,I+1):
    q.append(i)

while len(q) != 1:
    tmp = q.popleft()
    tmp2 = q.popleft()
    q.append(tmp2)

print(q.popleft())