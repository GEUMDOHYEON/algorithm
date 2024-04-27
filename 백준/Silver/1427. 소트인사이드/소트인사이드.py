N=list(input())
result = []

for i in sorted(N,reverse=True):
    result.append(int(i))
for i in result:
    print(i,end="")