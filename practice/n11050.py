import sys
sys.setrecursionlimit(10**7)

# 재귀 함수는 메모리 초과 -> 반복문으로 구현함.
# def factorial(N):
#     if N == 1:
#         return 1
#     return N * factorial(N-1)
def factorial(N):
    result = 1
    for i in range(1, N+1):
        result *= i
    return result

N, K = map(int,input().split())

result = factorial(N) / (factorial(K) * factorial((N-K)))

print(int(result))  