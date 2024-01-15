# a = [6,4,3,7,1,9,8]
##########################################################
######## 버블 정렬 ########
# for i in range(len(a) - 1):
#     count = 0   

#     for j in range(len(a) - i - 1):
#         if a[j] > a[j+1]:
#             tmp = a[j]
#             a[j] = a[j+1]
#             a[j+1] = tmp
#             count += 1
#     if count == 0:  # 정렬이 일어나지 않으면 이미 다 정렬됐다고 판단하여 정렬을 끝냄.
#         break
# print(a)

######## 선택 정렬 ########
# a = [3,2,4,5,1]

# for i in range(len(a) - 1):
#     min = i
#     for j in range(i+1,len(a)):
#         if a[min] > a[j]:
#             min = j
#     tmp = a[min]
#     a[min] = a[i]
#     a[i] = tmp

# print(a)

######## 삽입 정렬 ########
# for i in range(1,len(a)):
#     tmp = a[i]
#     idx = 0
#     for j in range(len(a)):
#         if tmp < a[j]:
#             idx = j
#         e = a[idx]
#         a[idx] = a[i]
#         a[i] = e

#     # while j > 0 and a[j-1] > tmp:
#     #     a[j] = a[j - 1]
#     #     j -= 1
#     # a[j] = tmp        
# print(a)

######## 퀵 정렬 ########
a = [0,1,2,4,3]

def qsort(a,left,right):
    pl = left
    pr = right
    x = a[(left + right) // 2]

    while pl <= pr:
        while a[pl] < x:
            pl += 1
        while a[pr] > x:
            pr -= 1
        if pl <= pr:
            tmp = a[pr]
            a[pr] = a[pl]
            a[pl] = tmp 
            pl += 1
            pr -= 1
    if left < pr:
        qsort(a,left,pr)
    if pl < right:
        qsort(a,pl,right)

qsort(a,0,len(a)-1)

print(a)