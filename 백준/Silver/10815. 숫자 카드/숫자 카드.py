import sys

N = int(sys.stdin.readline())

have_card = set(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

compare_card = list(map(int,sys.stdin.readline().split()))

for i in compare_card:
    if i in have_card:
        print(1, end=" ")
    else:
        print(0,end=" ")
        