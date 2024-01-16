import sys

num = int(input())
array = []

for i in range(num):
    array.append(int(sys.stdin.readline()))

for i in sorted(array):
    print(i)

###### 퀵 정렬 ######
# 책으로 배웠던 퀵정렬을 이용해 2751 소수찾기를 구현해보았다.
# 퀵정렬은 빠른 알고리즘이고 평균 시간복잡도가 O(nlogn)지만 최악의 경우 O(N^2)가 나와 시간초과로 인해 실패를 받게되었다.
# 나중에 병합정렬이나 힙정렬을 공부해 다시 풀어봐야겠다.
# for i in range(num):
#     array.append(int(sys.stdin.readline()))

# def qsort(a,left,right):
#     n = len(a)
#     pl = left
#     pr = right
#     x = a[(left + right) // 2]

#     while pl <= pr:
#         while a[pl] < x:
#             pl += 1
#         while a[pr] > x:
#             pr -= 1
#         if pr >= pl:
#             a[pl],a[pr] = a[pr],a[pl]
#             pl += 1
#             pr -= 1

#     if left < pr:
#         qsort(a,left,pl)
#     if right > pl:
#         qsort(a,pl,right)
        
# qsort(array,0,len(array)-1)

# for i in array:
#     print(i)