import sys

N = int(sys.stdin.readline())   # 노드의 개수
A = list(map(int, sys.stdin.readline().split())) # 수열
O = list(map(int, sys.stdin.readline().split())) # 연산자의 수

maximum = -1e+9 # 최댓값
minimum = 1e+9 # 최솟값

def dfs(sum,depth,plus,minus,multiply,divide):
    global maximum, minimum

    if depth == N:
        maximum = max(sum,maximum)
        minimum = min(sum,minimum)
        return
    
    if plus:
        dfs(sum+A[depth],depth+1,plus - 1, minus,multiply,divide)
    if minus:
        dfs(sum-A[depth],depth+1,plus, minus - 1,multiply,divide)
    if multiply:
        dfs(sum*A[depth],depth+1,plus, minus,multiply - 1,divide)
    if divide:
        dfs(int(sum/A[depth]),depth+1,plus, minus,multiply,divide - 1)



dfs(A[0],1,O[0],O[1],O[2],O[3])
print(maximum)
print(minimum)