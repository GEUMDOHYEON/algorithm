import sys

read = sys.stdin.readline

N, K = map(int,read().split())
item = list(map(int,read().split()))

count = 0

tab = []

for i in range(K):
    if item[i] in tab:
        continue

    if len(tab) != N:
        tab.append(item[i])
        continue

    pop_item = 0
    late_item = 0

    for t in tab:
        if t not in item[i:]:
            pop_item = t
            break
        elif item[i:].index(t) > late_item:
            late_item = item[i:].index(t)
            pop_item = t
    count += 1
    tab[tab.index(pop_item)] = item[i]

print(count)