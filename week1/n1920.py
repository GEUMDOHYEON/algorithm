n = int(input())
a1 = list(map(int,input().split()))
a1.sort()

m = int(input())
a2 = list(map(int,input().split()))

def bSearch(a,target,left,right):

    mid = (left + right) // 2

    if left > right:
        return 0
    
    if target == a[mid]:
        return 1
    elif a[mid] > target:
        return bSearch(a,target,left,mid-1)
    elif a[mid] < target:
        return bSearch(a,target,mid+1,right)


for i in range(m):
    print(bSearch(a1,a2[i],0,len(a1) - 1))

# for i in a1:
#     for i in a2:
#         print(i)