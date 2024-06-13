N = int(input())

arr = list(map(int,input().split()))
tmp = set(arr)
count = 0
result = {}

for i in sorted(tmp):
  result[i] = count
  count += 1

for i in arr:
    print(result[i],end=" ")