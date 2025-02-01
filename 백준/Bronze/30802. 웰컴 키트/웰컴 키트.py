import sys

N = int(sys.stdin.readline())
t_shirt = list(map(int,sys.stdin.readline().split()))
T,P = map(int,sys.stdin.readline().split())

# 티셔츠
t_bundle = 0
for i in t_shirt:
  tmp = i // T
  if i == 0:
    continue
  elif i <= T:
    t_bundle += 1
  elif i % T == 0:
    t_bundle += i // T
  else:
    t_bundle += (tmp + 1)


# 펜
pen_bundle = N // P
pen_remain = N % P

print(t_bundle)
print(pen_bundle,pen_remain)