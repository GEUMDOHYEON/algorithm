import math

t = int(input()) # 테스트 케이스 개수 입력

def is_prime(num): # 소수를 구하는 함수.
    if num == 1:
        return False
    for i in range(2,int(math.sqrt(num) + 1)): # 제곱근으로 구하는 이유는 반복 횟수 줄이기 위해
        if num % i == 0:
            return False
    return True

for i in range(t): # 테스트케이스 개수만큼 반복
    n = int(input()) # 골드바흐의 수

    # 골드바흐의 파티션 변수들
    a = n // 2 
    b = n // 2

    for j in range(n//2): # n을 2로 나누는 이유는 반복 횟수 줄이기 위해
        if is_prime(a) and is_prime(b): 
            print(a, b)
            break
        else:
            a -= 1
            b += 1


## 처음에 짠 골드바흐의 추측 코드 --> 두 소수의 차이가 가장 작은 것만 출력되어야 하는데 모두 출력하고있음.나중에 수정해보자.
# for i in range(t):
#     n = int(input())
    
#     array = [True for i in range(n+1)]

#     for j in range(2,int(math.sqrt(n) + 1)):
#         if array[j] == True:
#             k  = 2
#             while j * k <= n:
#                 array[k*j] = False
#                 k += 1

#     for o in range(2, n+1):
#         if array[o]:
#             for l in range(2,n+ 1):
#                 if array[l]:
#                     if n - o == l:
#                         print(o, l)
