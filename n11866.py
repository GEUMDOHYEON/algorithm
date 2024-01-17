N,K = list(map(int,input().split()))

jose = []

result = []

for i in range(N):
    jose.append(i+1)

while jose:
    tmp1 = jose[K-1:]
    tmp2 = jose[:K-1]
    jose = tmp1 + tmp2
    result.append(jose.pop(0))

print('<',end="")
for i in range(len(result)-1):
    print(result[i],end=", ")
print(result[len(result)-1],end="")
print('>')

# while jose:
#     for i in range(K-1):
#         jose.append(jose.pop(0))
#     result.append(jose.pop(0))
