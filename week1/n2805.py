import sys

N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))

start, end = 1, sum(trees)

while start <= end:
    goal = (start + end) // 2
    count = 0

    for tree in trees:
        if goal < tree:
            tmp = tree - goal
            count += tmp
    if M <= count:
        start = goal + 1
    else:
        end = goal -1

print(end)