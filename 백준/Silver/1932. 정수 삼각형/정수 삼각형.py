import sys

N = int(sys.stdin.readline())
triangle = []
result = 0

for _ in range(N):
    S = list(map(int,sys.stdin.readline().split()))
    triangle.append(S)


for i in range(1,N):
    for j in range(len(triangle[i])):
        if j == 0:
            triangle[i][0] += triangle[i-1][0]
        elif j == i:
            triangle[i][j] += triangle[i-1][j-1]
        else:
            triangle[i][j] += max(triangle[i-1][j-1],triangle[i-1][j])

print(max(triangle[N-1]))