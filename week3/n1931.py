import sys

N = int(sys.stdin.readline())
count = 0
tmp_b = 0
time = []

for i in range(N):
    a, b = map(int,sys.stdin.readline().split())
    time.append([a,b])

time.sort(key=lambda x:x[1])

for i in range(N):
    if time[i][0] >= tmp_b:
        count += 1
        tmp_b = time[i][1]

print(count)