import sys

read = sys.stdin.readline

N = int(read())

haveCard = list(map(int,read().split()))
haveCard.sort()

M = int(read())

findCard = list(map(int,read().split()))

result = []

count = {}

for card in haveCard:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

def bsf(a,b,left,right):
    if left>right:
        return 0
    
    mid = (left + right) // 2

    if a[mid] == b:
        return count.get(b)
    elif a[mid] < b:
        return bsf(a,b,mid+1,right)
    else:
        return bsf(a,b,left,mid-1)

for _ in findCard:
    print(bsf(haveCard,_,0,len(findCard)-1),end=" ")
