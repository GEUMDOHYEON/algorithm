import sys

read = sys.stdin.readline

K = int(read())

length = list(map(int,read().split()))
oil = list(map(int,read().split()))
result = 0

tmp = oil[0]
for i in range(K-1):
    if tmp > oil[i]:
        tmp = oil[i]
    result += tmp * length[i]


print(result)
            