import sys

read = sys.stdin.readline

N = int(read())

time = list(map(int,read().split()))

time.sort()

wait = []
tmp = 0
for i in range(N):
    tmp += time[i]
    wait.append(tmp)

result =0

for i in range(len(wait)):
    result += wait[i]

print(result)