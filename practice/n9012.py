N = int(input())

for i in range(N):
    ps = list(input())

    stack = []
    
    for p in ps: 
        if p == '(':
            stack.append(p)
        elif p == ')':
            if not stack:
                stack.append(p)
                break
            else:
                stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')
