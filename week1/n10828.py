import sys

N = int(sys.stdin.readline())
array =[]
    
for i in range(N):
    s = sys.stdin.readline().split()

    if s[0] == 'push':
        array.append(s[1])
    elif s[0] == 'pop':
        if len(array) == 0:
            print(-1)
        else:
            print(array.pop()) 
    elif s[0] == 'size':
        print(len(array))

    elif s[0] == 'empty':
        if len(array) == 0:
            print(1)
        else:
            print(0)
    elif s[0] == 'top':
        if len(array) == 0:
            print(-1)
        else: 
            print(array[-1]) 