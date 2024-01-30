import sys

read = sys.stdin.readline

A = read().strip()
B = read().strip()

memo = [[0] * (len(A) + 1) for _ in range(len(B) + 1)]

for i in range(1,len(B) + 1):
    for j in range(1,len(A) + 1):
        if A[j-1] == B[i-1]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j],memo[i][j-1])

print(memo[-1][-1])

answer = ""

i = len(B)
j = len(A)
        
while i>0 and j>0:
    if memo[i][j] == memo[i][j-1]:
        j-=1
    elif memo[i][j] == memo[i-1][j]:
        i-=1
    else:
        answer = B[i-1] + answer
        i-=1; j-=1

print(answer)