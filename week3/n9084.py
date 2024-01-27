import sys

T = int(sys.stdin.readline()) # 테스트 케이스의 수

for i in range(T):
    N = int(sys.stdin.readline()) # 동전의 가지 수
    coin = list(map(int,sys.stdin.readline().split())) # 동전의 각 금액
    cost = int(sys.stdin.readline()) # 동전으로 나눌 값

    memo = [0] * (cost + 1) # 메모이제이션을 위한 배열
    memo[0] = 1 # 모든 동전들이 0원을 만들기 위해서는 아무것도 안 내도 되므로 경우의 수는 1

    for i in range(len(coin)): # 각 동전마다 검사를 해야하기 때문.
        for j in range(1,cost+1): 
            if coin[i] <= j:
                memo[j] += memo[j - coin[i]] # 점화식

    print(memo[cost])
