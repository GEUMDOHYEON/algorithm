n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

# Please write your code here.
result = 0

S = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,0),(0,1),(1,-1),(1,0),(1,1)]

def checkCoin(x,y):
    coin = 0
    for s in S:
        dx = x + s[0]
        dy = y + s[1]
        if 0 <= dx < n and 0 <= dy < n:
            if grid[dx][dy] == 1:
                coin += 1
        else:
            coin = 0
            break
    return coin

for i in range(n):
    for j in range(n):
        result = max(result, checkCoin(i,j))

print(result)