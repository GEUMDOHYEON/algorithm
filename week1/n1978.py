import sys

n = int(sys.stdin.readline())
r = 0

a = list(map(int,sys.stdin.readline().split()))

for i in a:
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c += 1
    if c == 0 and i > 1:
        r += 1

print(r)

