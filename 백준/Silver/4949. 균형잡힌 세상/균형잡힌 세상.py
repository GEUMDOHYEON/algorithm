t = True

while t:
    stack = []
    str = input()
    if str == ".":
        break
    balanced = True
    for s in str:
        if s == "(" or s == "[":
           stack.append(s)
        elif s == ")":
            if not stack or stack[-1] != '(':
                balanced = False
                break
            stack.pop()
        elif s == "]":
            if not stack or stack[-1] != '[':
                balanced = False
                break
            stack.pop()
    if not stack and balanced:
        print("yes")
    else:
        print("no")
