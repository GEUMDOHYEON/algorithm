import sys
# import copy

# N = int(sys.stdin.readline())

# have_card = set(map(int,sys.stdin.readline().split()))

# M = int(sys.stdin.readline())

# compare_card = list(map(int,sys.stdin.readline().split()))
# c_card = copy.deepcopy(compare_card)
# compare_card.sort()

# tmp = []
# result = []

# for i in have_card:
#     s_idx = 0
#     e_idx = len(compare_card) - 1

#     while (s_idx <= e_idx):
#         m_idx = (s_idx + e_idx) // 2

#         if(compare_card[m_idx] == i):
#             tmp.append(i)
#             break
        
#         elif(compare_card[m_idx] < i):
#             s_idx = m_idx + 1
#             continue
#         if(compare_card[m_idx] > i):
#             e_idx = m_idx - 1
#             continue

# for i in c_card:
#     if i in tmp:
#         result.append(1)
#     else:
#         result.append(0)

# for i in result:
#     print(i,end=" ")


N = int(sys.stdin.readline())

have_card = set(map(int,sys.stdin.readline().split()))

M = int(sys.stdin.readline())

compare_card = list(map(int,sys.stdin.readline().split()))

for i in compare_card:
    if i in have_card:
        print(1, end=" ")
    else:
        print(0,end=" ")