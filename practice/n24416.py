import sys

read = sys.stdin.readline

N = int(read())

count = 0

memo = [0] * (N + 1)

def fibonacci(N):
    global count

    memo[1] = 1
    memo[2] = 1

    if N == 1 or N == 2: 
        return 1
    
    for i in range(3,N+1):
        count += 1
        memo[i] = memo[i-2] + memo[i-1]

    return memo[N]

print(fibonacci(N),count)

# def fibo(N): # 재귀 함수
#     global count

#     if N == 1 or N == 2:
#         return 1
#     count[0] += 1
#     return fibo(N-1) + fibo(N-2)