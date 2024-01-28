import sys

A = sys.stdin.readline().strip() # 문자열 1
B = sys.stdin.readline().strip() # 문자열 2

memo = [[0] * (len(A)+1) for _ in range(len(B) + 1)] # 문자열 비교를 위한 배열

for i in range(1,len(B)+1):
    for j in range(1,len(A)+1):
        if B[i-1] == A[j-1]: # 문자열1과 문자열2의 문자가 일치 할때
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i][j-1],memo[i-1][j]) 

print(memo[-1][-1])
