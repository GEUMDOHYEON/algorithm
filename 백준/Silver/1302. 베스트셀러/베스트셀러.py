import sys

N = int(sys.stdin.readline())

books = {}
for i in range(N):
    tmp = sys.stdin.readline().strip()
    if tmp in books:
        books[tmp] += 1
    else:
        books[tmp] = 1

best = []
for k,v in books.items():
    if v == max(books.values()):
        best.append(k)
        
best.sort()
print(best[0])
