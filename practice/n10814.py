import sys

read = sys.stdin.readline

N = int(read())
member = []

for i in range(N):
    age, name = read().split()
    member.append([int(age),name])

for i in sorted(member,key=lambda x : x[0]):
    print(i[0], i[1])