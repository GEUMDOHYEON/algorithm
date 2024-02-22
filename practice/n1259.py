while True:
    N = input()

    if N == '0':
        break
    elif N == N[::-1]:
        print('yes')
    else:
        print('no')

# mid = 0
# N = 1
# while True: 
#     N = input()
#     if N == '0':
#         break

    # is_palindrome = True    
#     front = []
#     back = []
#     mid = len(N) // 2    
#     if len(N) % 2 != 0:
#         for i in range(0,mid):
#             front.append(N[i])
#         for i in range(mid+1,len(N)):   
#             back.append(N[i])
#     else:
#         for i in range(mid):
#             front.append(N[i])

#         for i in range(mid,len(N)):
#             back.append(N[i])

#     back.reverse()

#     for i in range(mid):
#         if front[i] != back[i]:
#             is_palindrome = False
#             break
#         else:
#             is_palindrome = True

#     if is_palindrome:
#         print('yes')
#     else:
#         print('no')
