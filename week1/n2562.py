import sys

a = []

for i in range(9):
    a.append(int(sys.stdin.readline()))

print(max(a))
print(a.index(max(a))+1)

# x = a[0]
# s = 0

# for i in range(len(a)):
#     if x < a[i]:
#         x = a[i]
#         s = i + 1
    
# print(x)
# print(s)