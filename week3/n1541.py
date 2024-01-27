expressions = input()

expressions = expressions.split('-')
result = 0

for i in expressions[0].split('+'):
    result += int(i)
for i in expressions[1:]:
    for j in i.split('+'):
        result -= int(j)

# for expression in expressions: # 처음에 구현한 코드. +만 있을 땐 안됨.
#     if '+' in expression:
#         result -= eval(expression)
#     else:
#         result += int(expression)


print(result)