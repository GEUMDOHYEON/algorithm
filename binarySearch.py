a = [1,4,6,9,7]

a.sort()
n = 4

left = 0
right = len(a) - 1

def bSearch(n,left,right):
    if left > right:
        return 0

    left = left
    right = right
    mid = (left + right) // 2

    if a[mid] == n:
        return mid
    if a[mid] > n:
        return bSearch(n,left,mid-1)
    if a[mid] < n:
        return bSearch(n,mid+1,right)

print(bSearch(5,0,len(a)-1))