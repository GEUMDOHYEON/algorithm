import sys

N = int(sys.stdin.readline())
costs = list(map(int,sys.stdin.readline().split()))
M = int(sys.stdin.readline())

costs.sort()

pl,pr = 0, max(costs)

while pl <= pr:
    mid = (pl + pr) // 2
    total = 0
    for i in costs:
        if i > mid:
            total += mid
        else:
            total += i
    if total > M: 
        pr = mid - 1
    else:
        pl = mid + 1

print(pr)