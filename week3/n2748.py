import sys

N = int(sys.stdin.readline())
fibo = [0] * (N+1) # 메모이제이션을 위한 리스트.

def fibonacci(N): # 피보나치 함수 -> 재귀함수로 구현. 탑-다운 방식
    global fibo

    if N == 1 or N == 2:
        return 1
    if fibo[N] != 0:
        return fibo[N]
    
    fibo[N] = fibonacci(N-1) + fibonacci(N-2)
    print(fibo)
    
    return fibo[N]
    
print(fibonacci(N))