##### 피보나치 수열의 합 구하기 (for 문 이용)

# def fibo(n):
#     a,b = 1,1
#     if n == 1 or n == 2:
#         return 1
#     for i in range(1,n):
#         a, b =b,a+b
#     return a

# print(fibo(7))  

##### 피보나치 수열의 합 구하기 (재귀함수 이용)
def fibo(n):
    if n ==1 or n == 2:
        return 1
    return fibo(n-1) + fibo(n-2)

print(fibo(7))