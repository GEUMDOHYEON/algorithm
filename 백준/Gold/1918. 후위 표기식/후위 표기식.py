S = list(input())

def convert_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    result = ''
    stack = []

    for s in expression:
        if s.isalpha():
            result += s
        elif s == '(':
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # Remove '(' from stack
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(s, 0):
                result += stack.pop()
            stack.append(s)

    while stack:
        result += stack.pop()

    return result

print(convert_to_postfix(S))