from collections import deque
import sys

N = int(sys.stdin.readline())

array = deque()

for i in range(N):
    s = sys.stdin.readline().split()

    if s[0] == 'push':
        array.append(s[1])
    elif s[0] == 'pop':
        if array:
            print(array.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(array))
    elif s[0] == 'empty':
        if array:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if array:
            print(array[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if array:
            print(array[-1])
        else:
            print(-1)