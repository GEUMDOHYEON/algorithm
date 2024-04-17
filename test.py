N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
result = 0

A.sort()
B.sort(reverse=True)
print
for i in range(N):
    result += (A[i] * B[i])
print(result)