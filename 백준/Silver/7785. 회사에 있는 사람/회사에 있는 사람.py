import sys

n = int(sys.stdin.readline())
inOffice = {}

for i in range(n):
    name, status = map(str,sys.stdin.readline().split())
    if status == 'enter':
        inOffice[name] = True
    elif status == 'leave':
        del inOffice[name]

sorted(inOffice, reverse=True)

for i in sorted(inOffice, reverse=True):
    print(i)