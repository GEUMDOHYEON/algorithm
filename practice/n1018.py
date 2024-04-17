import sys

read = sys.stdin.readline

N, M = map(int,read().split())

board = []
count = []

for i in range(N):
    arr = list(read().strip())
    board.append(arr)

for i in range(N-7):
    for j in range(M-7):
        w = 0
        b = 0
        for x in range(i,i+8):
            for y in range(j,j+8):
                if (x+y) % 2 == 0:
                    if board[x][y] != 'W':
                        w += 1
                    if board[x][y] != 'B':
                        b += 1
                else:
                    if board[x][y] != 'B':
                        w += 1
                    if board[x][y] != 'W':
                        b += 1
        count.append(min(w,b))

print(min(count))
            
